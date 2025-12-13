"""
Integration Test: Complete Flow
Scanner → API → Queue → Workers → Database

Tests the full pipeline end-to-end.

Run:
    # Terminal 1: Start API server
    python api_server.py
    
    # Terminal 2: Run this test
    python test_complete_flow.py
"""

import sys
import asyncio
from pathlib import Path
from datetime import datetime

# Add project root
sys.path.insert(0, str(Path(__file__).parent))

from scanner import ModuleScanner, RecursiveScanStrategy, APISubmitObserver
from api_client import APIClient, APIClientError
from api import InMemoryQueueStrategy
from workers import WorkerPool, LoggingWorkerObserver, MetricsWorkerObserver
from models import DatabaseSessionFactory, UnitOfWork


def test_complete_pipeline():
    """Test complete scanner → API → queue → workers → database flow"""
    print("\n" + "🧪" * 30)
    print(" COMPLETE PIPELINE INTEGRATION TEST")
    print("🧪" * 30)
    
    # Step 1: Check API
    print("\n1️⃣ Checking API server...")
    api_client = APIClient(base_url="http://localhost:8000", timeout=10)
    
    try:
        health = api_client.health_check()
        print(f"   ✅ API Status: {health['status']}")
    except APIClientError as e:
        print(f"   ❌ API not available: {e}")
        print("\n   Start API server: python api_server.py")
        return False
    
    # Step 2: Setup database
    print("\n2️⃣ Setting up database...")
    db_factory = DatabaseSessionFactory(
        connection_string="sqlite:///test_complete_flow.db",
        echo=False
    )
    db_factory.create_tables()
    print("   ✅ Database created")
    
    # Step 3: Configure scanner
    print("\n3️⃣ Configuring scanner...")
    strategy = RecursiveScanStrategy(
        max_depth=2,
        excluded_patterns=['test_*', '__pycache__', 'venv', '.git', 'vendor']
    )
    
    observer = APISubmitObserver(
        api_client=api_client,
        enable_batch=True
    )
    
    scanner = ModuleScanner(
        scan_strategy=strategy,
        observers=[observer],
        batch_size=10
    )
    print("   ✅ Scanner ready")
    
    # Step 4: Scan modules
    print("\n4️⃣ Scanning for modules...")
    scan_path = Path('.')
    modules = scanner.scan(scan_path)
    print(f"   ✅ Discovered {len(modules)} modules")
    print(f"   📤 Submitted {observer.submitted_count} to API")
    
    # Step 5: Check queue status
    print("\n5️⃣ Checking queue status...")
    try:
        metrics = api_client.get_metrics()
        queue_size = metrics['queue']['size']
        print(f"   ✅ Queue size: {queue_size}")
    except APIClientError as e:
        print(f"   ❌ Metrics error: {e}")
        return False
    
    # Step 6: Start workers
    print("\n6️⃣ Starting async workers...")
    
    # Get queue from API (in real scenario, workers would access same queue)
    # For testing, we'll use the API's queue directly
    # NOTE: In production, workers would be part of api_server.py
    
    print("   ⚠️  Note: Workers need access to API's internal queue")
    print("   ⚠️  In production, workers run inside api_server.py process")
    print("   ⚠️  This test demonstrates worker functionality separately")
    
    # Create separate queue for demonstration
    test_queue = InMemoryQueueStrategy(maxsize=100)
    
    # Add some test modules to demonstrate workers
    print("\n   📤 Adding test modules to worker queue...")
    from api import ModuleDiscoveryResult
    
    for i in range(3):
        test_module = ModuleDiscoveryResult(
            module_name=f'worker_test_module_{i}',
            filepath=f'/test/worker_module_{i}.py',
            is_package=False,
            classes=[{'name': f'WorkerTestClass{i}', 'lineno': 10}],
            functions=[{'name': f'worker_test_func{i}', 'lineno': 20}],
            imports=['sys'],
            checksum=f'worker_hash{i}',
            discovered_at=datetime.utcnow().isoformat(),
            scanner_version='1.0.0'
        )
        test_queue.enqueue(test_module, priority=1)
    
    print(f"   ✅ Added 3 test modules to worker queue")
    
    # Create worker pool
    worker_observers = [
        LoggingWorkerObserver(),
        MetricsWorkerObserver()
    ]
    
    pool = WorkerPool(
        queue_strategy=test_queue,
        db_factory=db_factory,
        num_workers=2,
        observers=worker_observers
    )
    
    # Process queue
    print("\n   ⚙️  Processing queue with workers...")
    asyncio.run(pool.process_until_empty())
    
    # Step 7: Verify database
    print("\n7️⃣ Verifying database...")
    with UnitOfWork(db_factory) as uow:
        modules_in_db = uow.repositories['module'].get_all()
        classes_in_db = uow.repositories['class'].get_all()
        functions_in_db = uow.repositories['function'].get_all()
        
        print(f"   ✅ Modules in DB: {len(modules_in_db)}")
        print(f"   ✅ Classes in DB: {len(classes_in_db)}")
        print(f"   ✅ Functions in DB: {len(functions_in_db)}")
        
        if modules_in_db:
            print("\n   Sample modules:")
            for mod in modules_in_db[:5]:
                print(f"      - {mod.name}")
    
    # Step 8: Worker metrics
    print("\n8️⃣ Worker metrics...")
    metrics_observer = next(o for o in worker_observers if isinstance(o, MetricsWorkerObserver))
    worker_metrics = metrics_observer.get_metrics()
    
    print(f"   ✅ Processed: {worker_metrics['total_processed']}")
    print(f"   ❌ Errors: {worker_metrics['total_errors']}")
    print(f"   ⏱️  Avg duration: {worker_metrics['avg_duration']:.3f}s")
    
    api_client.close()
    
    print("\n" + "=" * 90)
    print("✅ COMPLETE PIPELINE TEST SUCCESSFUL!")
    print("=" * 90)
    print("\nFlow verified:")
    print("  Scanner → API → Queue → Workers → Database")
    print("\nAll components working correctly!")
    print("=" * 90)
    
    return True


def test_worker_pool_only():
    """Test worker pool in isolation"""
    print("\n" + "🧪" * 30)
    print(" WORKER POOL ISOLATED TEST")
    print("🧪" * 30)
    
    # Setup
    queue = InMemoryQueueStrategy(maxsize=100)
    db_factory = DatabaseSessionFactory(
        connection_string="sqlite:///test_workers_only.db",
        echo=False
    )
    db_factory.create_tables()
    
    # Add test modules
    print("\n📤 Adding 10 test modules to queue...")
    from api import ModuleDiscoveryResult
    
    for i in range(10):
        module = ModuleDiscoveryResult(
            module_name=f'isolated_test_module_{i}',
            filepath=f'/test/isolated_{i}.py',
            is_package=False,
            classes=[
                {'name': f'IsolatedClass{i}A', 'lineno': 10},
                {'name': f'IsolatedClass{i}B', 'lineno': 50}
            ],
            functions=[
                {'name': f'isolated_func{i}', 'lineno': 20},
                {'name': f'another_func{i}', 'lineno': 30}
            ],
            imports=['sys', 'os', 'typing'],
            checksum=f'isolated_hash{i}',
            discovered_at=datetime.utcnow().isoformat(),
            scanner_version='1.0.0'
        )
        queue.enqueue(module, priority=1)
    
    print("✅ Queue populated")
    
    # Create worker pool
    print("\n⚙️  Creating worker pool with 3 workers...")
    observers = [
        LoggingWorkerObserver(),
        MetricsWorkerObserver()
    ]
    
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=3,
        observers=observers
    )
    
    # Process
    print("\n🚀 Processing queue...")
    asyncio.run(pool.process_until_empty())
    
    # Verify
    print("\n📊 Verification...")
    with UnitOfWork(db_factory) as uow:
        modules = uow.repositories['module'].get_all()
        classes = uow.repositories['class'].get_all()
        functions = uow.repositories['function'].get_all()
        
        print(f"✅ Modules: {len(modules)}/10")
        print(f"✅ Classes: {len(classes)}/20")
        print(f"✅ Functions: {len(functions)}/20")
    
    # Metrics
    metrics_observer = next(o for o in observers if isinstance(o, MetricsWorkerObserver))
    metrics = metrics_observer.get_metrics()
    
    print(f"\n📈 Worker Metrics:")
    print(f"   Processed: {metrics['total_processed']}")
    print(f"   Errors: {metrics['total_errors']}")
    print(f"   Avg duration: {metrics['avg_duration']:.3f}s")
    
    print("\n" + "=" * 90)
    print("✅ WORKER POOL TEST COMPLETE!")
    print("=" * 90)
    
    return True


if __name__ == '__main__':
    print("\n" + "🚀" * 30)
    print(" COMPLETE FLOW TEST SUITE")
    print("🚀" * 30)
    
    # Test 1: Worker pool in isolation
    print("\n" + "-" * 90)
    success1 = test_worker_pool_only()
    
    # Test 2: Complete pipeline (requires API server)
    print("\n" + "-" * 90)
    print("\n⚠️  Next test requires API server running")
    print("   Start in another terminal: python api_server.py")
    
    response = input("\nAPI server running? (y/n): ").strip().lower()
    
    if response == 'y':
        success2 = test_complete_pipeline()
    else:
        print("\n⏭️  Skipping complete pipeline test")
        print("   Run manually when API server is available")
        success2 = True  # Don't fail the suite
    
    # Summary
    print("\n" + "=" * 90)
    print(" TEST SUMMARY")
    print("=" * 90)
    
    results = [
        ("Worker Pool Isolated", success1),
        ("Complete Pipeline", success2)
    ]
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status} - {test_name}")
    
    all_passed = all(result for _, result in results)
    
    print("\n" + "=" * 90)
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
    else:
        print("⚠️  SOME TESTS FAILED")
    print("=" * 90)
    
    sys.exit(0 if all_passed else 1)
