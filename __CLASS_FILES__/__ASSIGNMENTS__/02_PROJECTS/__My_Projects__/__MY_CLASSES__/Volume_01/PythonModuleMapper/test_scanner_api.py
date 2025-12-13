"""
Integration Test: Scanner → API → Queue

Tests the complete flow:
1. Start scanner with API client
2. Discover modules recursively
3. Submit to API in batches
4. Verify queue reception

Run:
    # Terminal 1: Start API server
    python api_server.py
    
    # Terminal 2: Run this test
    python test_scanner_api.py
"""

import sys
from pathlib import Path
from datetime import datetime

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from scanner import ModuleScanner, RecursiveScanStrategy, APISubmitObserver
from api_client import APIClient, APIClientError


def test_scanner_api_integration():
    """Test complete scanner → API integration"""
    print("\n" + "🧪" * 30)
    print(" Scanner → API Integration Test")
    print("🧪" * 30)
    
    # Step 1: Check API availability
    print("\n1️⃣ Checking API server...")
    api_client = APIClient(
        base_url="http://localhost:8000",
        timeout=10,
        retry_attempts=2
    )
    
    try:
        health = api_client.health_check()
        print(f"   ✅ API Status: {health['status']}")
        print(f"   📊 Initial queue size: {health['queue']['size']}")
    except APIClientError as e:
        print(f"   ❌ API not available: {e}")
        print("\n   Start the API server:")
        print("   python api_server.py")
        return False
    
    # Step 2: Configure scanner
    print("\n2️⃣ Configuring scanner...")
    
    strategy = RecursiveScanStrategy(
        max_depth=2,  # Limit depth for testing
        excluded_patterns=['test_*', '*_test', '__pycache__', 'venv', '.git']
    )
    
    observer = APISubmitObserver(
        api_client=api_client,
        enable_batch=True  # Use batch submission
    )
    
    scanner = ModuleScanner(
        scan_strategy=strategy,
        observers=[observer],
        batch_size=10
    )
    
    print("   ✅ Scanner configured with:")
    print(f"      Strategy: RecursiveScanStrategy (max_depth=2)")
    print(f"      Observer: APISubmitObserver (batch mode)")
    print(f"      Batch size: 10 modules")
    
    # Step 3: Scan current directory
    print("\n3️⃣ Scanning modules...")
    scan_path = Path('.')
    print(f"   Path: {scan_path.absolute()}")
    
    try:
        modules = scanner.scan(scan_path)
        print(f"   ✅ Discovered {len(modules)} modules")
        
        # Show sample of discovered modules
        if modules:
            print(f"\n   Sample modules:")
            for module in modules[:5]:
                print(f"      - {module}")
            if len(modules) > 5:
                print(f"      ... and {len(modules) - 5} more")
    
    except Exception as e:
        print(f"   ❌ Scan error: {e}")
        return False
    
    # Step 4: Verify API submission
    print("\n4️⃣ Verifying API submission...")
    
    try:
        metrics = api_client.get_metrics()
        queue_size = metrics['queue']['size']
        total_enqueued = metrics['queue']['total_enqueued']
        
        print(f"   ✅ Queue status:")
        print(f"      Current size: {queue_size}")
        print(f"      Total enqueued: {total_enqueued}")
        
        if 'processing' in metrics:
            print(f"      Total processed: {metrics['processing']['total_processed']}")
            print(f"      Total errors: {metrics['processing']['total_errors']}")
    
    except APIClientError as e:
        print(f"   ❌ Metrics error: {e}")
        return False
    
    # Step 5: Check observer stats
    print("\n5️⃣ Observer statistics...")
    print(f"   ✅ Submitted: {observer.submitted_count}")
    print(f"   ❌ Errors: {observer.error_count}")
    print(f"   📊 Success rate: {observer.submitted_count / (observer.submitted_count + observer.error_count) * 100:.1f}%" if (observer.submitted_count + observer.error_count) > 0 else "   N/A")
    
    # Step 6: Final health check
    print("\n6️⃣ Final health check...")
    try:
        health = api_client.health_check()
        print(f"   ✅ API Status: {health['status']}")
        print(f"   📊 Final queue size: {health['queue']['size']}")
    except APIClientError as e:
        print(f"   ❌ Health check failed: {e}")
    
    api_client.close()
    
    print("\n" + "=" * 90)
    print("✅ Integration test complete!")
    print("=" * 90)
    return True


def test_single_module_submission():
    """Test submitting a single module"""
    print("\n" + "🧪" * 30)
    print(" Single Module Submission Test")
    print("🧪" * 30)
    
    api_client = APIClient(base_url="http://localhost:8000")
    
    try:
        # Check health first
        health = api_client.health_check()
        print(f"✅ API available: {health['status']}")
        
        # Create test module data
        test_module = {
            'module_name': 'test_integration_module',
            'filepath': '/test/path/module.py',
            'is_package': False,
            'classes': [{'name': 'TestClass', 'lineno': 10}],
            'functions': [{'name': 'test_func', 'lineno': 20}],
            'imports': ['sys', 'os'],
            'checksum': 'test123',
            'discovered_at': datetime.utcnow().isoformat(),
            'scanner_version': '1.0.0'
        }
        
        print("\n📤 Submitting test module...")
        result = api_client.submit_module(test_module)
        
        print(f"✅ Success!")
        print(f"   Queue ID: {result['queue_id']}")
        print(f"   Module: {result['module']}")
        print(f"   Status: {result['status']}")
        
        api_client.close()
        return True
        
    except APIClientError as e:
        print(f"❌ Test failed: {e}")
        api_client.close()
        return False


def test_batch_submission():
    """Test batch submission"""
    print("\n" + "🧪" * 30)
    print(" Batch Submission Test")
    print("🧪" * 30)
    
    api_client = APIClient(base_url="http://localhost:8000")
    
    try:
        # Create batch of test modules
        batch = [
            {
                'module_name': f'test_batch_module_{i}',
                'filepath': f'/test/path/module_{i}.py',
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
        
        print(f"📤 Submitting batch of {len(batch)} modules...")
        result = api_client.submit_batch(batch)
        
        print(f"✅ Batch submission complete!")
        print(f"   Total: {result['total']}")
        print(f"   Successful: {result['successful']}")
        print(f"   Failed: {result['failed']}")
        
        api_client.close()
        return True
        
    except APIClientError as e:
        print(f"❌ Batch test failed: {e}")
        api_client.close()
        return False


if __name__ == '__main__':
    print("\n" + "🚀" * 30)
    print(" SCANNER → API INTEGRATION TEST SUITE")
    print("🚀" * 30)
    
    # Check if API is running
    print("\n⚙️  Pre-flight check...")
    api_client = APIClient(base_url="http://localhost:8000", timeout=2)
    try:
        api_client.health_check()
        api_client.close()
        print("✅ API server is running\n")
    except:
        print("❌ API server not running!")
        print("\n📝 Start the API server in another terminal:")
        print("   python api_server.py")
        print("\n   Or:")
        print("   uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload")
        sys.exit(1)
    
    # Run tests
    test_results = []
    
    print("\n" + "-" * 90)
    test_results.append(("Single Module", test_single_module_submission()))
    
    print("\n" + "-" * 90)
    test_results.append(("Batch Submission", test_batch_submission()))
    
    print("\n" + "-" * 90)
    test_results.append(("Full Integration", test_scanner_api_integration()))
    
    # Summary
    print("\n" + "=" * 90)
    print(" TEST SUMMARY")
    print("=" * 90)
    
    for test_name, passed in test_results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status} - {test_name}")
    
    all_passed = all(result for _, result in test_results)
    
    print("\n" + "=" * 90)
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
    else:
        print("⚠️  SOME TESTS FAILED")
    print("=" * 90)
    
    sys.exit(0 if all_passed else 1)
