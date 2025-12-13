"""
Test Script for API Receiver Endpoint

Tests the complete flow:
1. Start API server (in background)
2. Submit modules via API client
3. Verify queue operation
4. Check health and metrics

Run:
    python test_api.py
"""

import sys
import time
import subprocess
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from api_client import APIClient, APIClientError


def test_api_endpoints():
    """Test all API endpoints"""
    print("🧪 Testing Module Discovery API")
    print("=" * 50)
    
    # Create client
    client = APIClient(
        base_url="http://localhost:8000",
        timeout=5,
        retry_attempts=2
    )
    
    # Test 1: Health check
    print("\n1️⃣ Testing health check...")
    try:
        health = client.health_check()
        print(f"   ✅ Status: {health['status']}")
        print(f"   📊 Queue size: {health['queue']['size']}")
    except APIClientError as e:
        print(f"   ❌ Health check failed: {e}")
        return False
    
    # Test 2: Submit single module
    print("\n2️⃣ Testing single module submission...")
    module_data = {
        'module_name': 'test_collections',
        'filepath': '/usr/lib/python3.9/collections.py',
        'is_package': False,
        'classes': [
            {'name': 'OrderedDict', 'lineno': 100},
            {'name': 'Counter', 'lineno': 200}
        ],
        'functions': [
            {'name': 'namedtuple', 'lineno': 50}
        ],
        'imports': ['sys', '_collections'],
        'checksum': 'abc123def456',
        'discovered_at': datetime.utcnow().isoformat(),
        'scanner_version': '1.0.0'
    }
    
    try:
        result = client.submit_module(module_data)
        print(f"   ✅ Submitted: {result['module']}")
        print(f"   🎫 Queue ID: {result['queue_id']}")
    except APIClientError as e:
        print(f"   ❌ Submission failed: {e}")
        return False
    
    # Test 3: Submit batch
    print("\n3️⃣ Testing batch submission...")
    batch_modules = [
        {
            'module_name': f'test_module_{i}',
            'filepath': f'/path/to/module_{i}.py',
            'is_package': False,
            'classes': [],
            'functions': [{'name': f'func_{i}', 'lineno': 10}],
            'imports': ['sys'],
            'checksum': f'hash_{i}',
            'discovered_at': datetime.utcnow().isoformat(),
            'scanner_version': '1.0.0'
        }
        for i in range(5)
    ]
    
    batch_result = client.submit_batch(batch_modules)
    print(f"   ✅ Successful: {batch_result['successful']}/{batch_result['total']}")
    print(f"   ❌ Failed: {batch_result['failed']}/{batch_result['total']}")
    
    # Test 4: Get metrics
    print("\n4️⃣ Testing metrics endpoint...")
    try:
        metrics = client.get_metrics()
        print(f"   ✅ Queue size: {metrics['queue']['size']}")
        print(f"   📈 Total enqueued: {metrics['queue']['total_enqueued']}")
        
        if 'processing' in metrics:
            print(f"   📊 Total processed: {metrics['processing']['total_processed']}")
    except APIClientError as e:
        print(f"   ❌ Metrics failed: {e}")
    
    # Test 5: Health check again
    print("\n5️⃣ Final health check...")
    try:
        health = client.health_check()
        print(f"   ✅ Status: {health['status']}")
        print(f"   📊 Queue size: {health['queue']['size']}")
    except APIClientError as e:
        print(f"   ❌ Health check failed: {e}")
    
    client.close()
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    return True


def check_server_running():
    """Check if API server is running"""
    client = APIClient(base_url="http://localhost:8000", timeout=2)
    try:
        client.health_check()
        client.close()
        return True
    except:
        return False


if __name__ == '__main__':
    print("\n" + "🚀" * 25)
    print(" Module Discovery API Test Suite")
    print("🚀" * 25)
    
    # Check if server is running
    if not check_server_running():
        print("\n⚠️  API server not running!")
        print("\n📝 Start the server in another terminal:")
        print("   python api_server.py")
        print("\n   Or:")
        print("   uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload")
        sys.exit(1)
    
    print("\n✅ API server is running")
    
    # Run tests
    success = test_api_endpoints()
    
    sys.exit(0 if success else 1)
