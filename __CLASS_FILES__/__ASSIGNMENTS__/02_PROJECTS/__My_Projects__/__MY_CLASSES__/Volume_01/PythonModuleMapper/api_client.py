"""
API Client for Module Scanner

Provides a client interface for scanner.py to submit modules to the API.
Uses dependency injection for configuration.

Usage:
    client = APIClient(api_config)
    result = client.submit_module(module_result)
"""

from typing import Dict, Any, Optional
from dataclasses import asdict
import requests
import json
from datetime import datetime


class APIClient:
    """
    Client for communicating with Module Discovery API.
    
    Dependency Injection:
    - base_url: API base URL (from config)
    - timeout: Request timeout in seconds
    - retry_attempts: Number of retry attempts
    """
    
    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        retry_attempts: int = 3,
        api_key: Optional[str] = None
    ):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.retry_attempts = retry_attempts
        self.api_key = api_key
        
        # Setup session
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}'
            })
        
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'ModuleScanner/1.0.0'
        })
    
    def submit_module(self, module_result: Any) -> Dict[str, Any]:
        """
        Submit a module discovery result to the API.
        
        Args:
            module_result: ModuleDiscoveryResult instance
        
        Returns:
            Response dictionary with status and queue_id
        
        Raises:
            APIClientError: If submission fails after retries
        """
        # Convert to dict
        if hasattr(module_result, '__dict__'):
            data = asdict(module_result) if hasattr(module_result, '__dataclass_fields__') else module_result.__dict__
        else:
            data = module_result
        
        url = f"{self.base_url}/api/v1/modules"
        
        for attempt in range(self.retry_attempts):
            try:
                response = self.session.post(
                    url,
                    json=data,
                    timeout=self.timeout
                )
                
                response.raise_for_status()
                return response.json()
            
            except requests.exceptions.HTTPError as e:
                if attempt == self.retry_attempts - 1:
                    raise APIClientError(f"HTTP error after {self.retry_attempts} attempts: {e}")
                continue
            
            except requests.exceptions.ConnectionError as e:
                if attempt == self.retry_attempts - 1:
                    raise APIClientError(f"Connection error after {self.retry_attempts} attempts: {e}")
                continue
            
            except requests.exceptions.Timeout as e:
                if attempt == self.retry_attempts - 1:
                    raise APIClientError(f"Timeout after {self.retry_attempts} attempts: {e}")
                continue
        
        raise APIClientError("Unknown error during submission")
    
    def submit_batch(self, module_results: list[Any]) -> Dict[str, Any]:
        """
        Submit multiple modules in batch.
        
        Args:
            module_results: List of ModuleDiscoveryResult instances
        
        Returns:
            Dictionary with success/failure counts and details
        """
        results = {
            'total': len(module_results),
            'successful': 0,
            'failed': 0,
            'details': []
        }
        
        for module_result in module_results:
            try:
                response = self.submit_module(module_result)
                results['successful'] += 1
                results['details'].append({
                    'module': getattr(module_result, 'module_name', 'unknown'),
                    'status': 'success',
                    'queue_id': response.get('queue_id')
                })
            except APIClientError as e:
                results['failed'] += 1
                results['details'].append({
                    'module': getattr(module_result, 'module_name', 'unknown'),
                    'status': 'failed',
                    'error': str(e)
                })
        
        return results
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check API health status.
        
        Returns:
            Health check response
        """
        url = f"{self.base_url}/api/v1/health"
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIClientError(f"Health check failed: {e}")
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get API metrics.
        
        Returns:
            Metrics response
        """
        url = f"{self.base_url}/api/v1/metrics"
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIClientError(f"Metrics request failed: {e}")
    
    def close(self):
        """Close the session"""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()


class APIClientError(Exception):
    """Custom exception for API client errors"""
    pass


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    # Example: Create client with dependency injection
    client = APIClient(
        base_url="http://localhost:8000",
        timeout=30,
        retry_attempts=3
    )
    
    # Example module data
    module_data = {
        'module_name': 'test_module',
        'filepath': '/path/to/test_module.py',
        'is_package': False,
        'classes': [],
        'functions': [{'name': 'test_func', 'lineno': 10}],
        'imports': ['sys'],
        'checksum': 'test123',
        'discovered_at': datetime.utcnow().isoformat(),
        'scanner_version': '1.0.0'
    }
    
    try:
        # Submit module
        result = client.submit_module(module_data)
        print("✅ Submission successful:", result)
        
        # Check health
        health = client.health_check()
        print("📊 Health:", health)
        
        # Get metrics
        metrics = client.get_metrics()
        print("📈 Metrics:", metrics)
    
    except APIClientError as e:
        print("❌ Error:", e)
    
    finally:
        client.close()
