# Running the Module Discovery System

## Complete System Test

### Step 1: Start the API Server

```bash
# Terminal 1
python api_server.py
```

**Expected Output**:
```
✅ Module Discovery API started
📊 Queue capacity: 1000 items
👀 Observers: LoggingObserver, MetricsObserver
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Verify**: Visit http://localhost:8000/docs for API documentation

---

### Step 2: Run the Scanner

```bash
# Terminal 2
python scanner.py
```

**Expected Output**:
```
============================================================
Example 1: Scanner with API Integration
============================================================
✅ API is available: healthy

Scanning: C:\...\PythonModuleMapper
Executing 15 scan commands...
Submitting batch of 15 modules to API...
✅ Batch submission complete:
   Success: 15/15
   Failed: 0/15

✅ Discovered 15 total modules
```

---

### Step 3: Run Integration Tests

```bash
# Terminal 2 (same as scanner)
python test_scanner_api.py
```

**Expected Output**:
```
🚀🚀🚀 SCANNER → API INTEGRATION TEST SUITE 🚀🚀🚀

✅ API server is running

✅ PASSED - Single Module
✅ PASSED - Batch Submission
✅ PASSED - Full Integration

🎉 ALL TESTS PASSED!
```

---

### Step 4: Check API Status

```bash
# Terminal 2
python test_api.py
```

**Expected Output**:
```
🧪 Testing Module Discovery API
==================================================

1️⃣ Testing health check...
   ✅ Status: healthy
   📊 Queue size: X

2️⃣ Testing single module submission...
   ✅ Submitted: test_collections
   🎫 Queue ID: queue_X_XXXX

...

✅ All tests completed!
```

---

## Quick Commands

### Check API Health
```bash
curl http://localhost:8000/api/v1/health
```

### Get Queue Metrics
```bash
curl http://localhost:8000/api/v1/metrics
```

### Submit Module Manually
```bash
curl -X POST http://localhost:8000/api/v1/modules \
  -H "Content-Type: application/json" \
  -d '{
    "module_name": "test_module",
    "filepath": "/path/to/module.py",
    "is_package": false,
    "classes": [],
    "functions": [],
    "imports": [],
    "checksum": "abc123",
    "scanner_version": "1.0.0"
  }'
```

---

## Programmatic Usage

### Using Scanner with API

```python
from scanner import ModuleScanner, RecursiveScanStrategy, APISubmitObserver
from api_client import APIClient
from pathlib import Path

# Create API client
api_client = APIClient(
    base_url="http://localhost:8000",
    timeout=30,
    retry_attempts=3
)

# Create scanner
strategy = RecursiveScanStrategy(max_depth=3)
observer = APISubmitObserver(api_client, enable_batch=True)
scanner = ModuleScanner(strategy, observers=[observer], batch_size=20)

# Scan and submit
modules = scanner.scan(Path('/path/to/code'))
print(f"Discovered {len(modules)} modules")

# Check results
metrics = api_client.get_metrics()
print(f"Queue size: {metrics['queue']['size']}")

api_client.close()
```

### Using API Client Directly

```python
from api_client import APIClient
from datetime import datetime

client = APIClient(base_url="http://localhost:8000")

# Submit single module
module_data = {
    'module_name': 'my_module',
    'filepath': '/path/to/my_module.py',
    'is_package': False,
    'classes': [{'name': 'MyClass', 'lineno': 10}],
    'functions': [{'name': 'my_func', 'lineno': 20}],
    'imports': ['sys'],
    'checksum': 'abc123',
    'discovered_at': datetime.utcnow().isoformat(),
    'scanner_version': '1.0.0'
}

result = client.submit_module(module_data)
print(f"Queue ID: {result['queue_id']}")

# Submit batch
batch = [module_data, ...]
batch_result = client.submit_batch(batch)
print(f"Success: {batch_result['successful']}/{batch_result['total']}")

client.close()
```

---

## Troubleshooting

### API Not Starting

**Error**: `Address already in use`

**Solution**: Change port
```python
# In api_server.py, change:
uvicorn.run("api_server:app", port=8001)
```

### Scanner Can't Connect

**Error**: `Connection refused`

**Solution**: Verify API is running
```bash
curl http://localhost:8000/api/v1/health
```

### No Modules Found

**Issue**: Scanner returns empty list

**Solutions**:
1. Check scan path: `Path.cwd()` shows current directory
2. Increase max_depth: `RecursiveScanStrategy(max_depth=5)`
3. Check exclusion patterns: Remove restrictive patterns

### Batch Submission Fails

**Issue**: All submissions fail in batch

**Solutions**:
1. Check API health: `api_client.health_check()`
2. Verify module data format matches API schema
3. Check logs in Terminal 1 (API server)
4. Enable single submission mode: `enable_batch=False`

---

## System Architecture

```
┌─────────────────────────────────────────────────┐
│              Scanner (scanner.py)                │
│  - RecursiveScanStrategy: Find .py files        │
│  - ScanModuleCommand: Extract with pyclbr       │
│  - ModuleScanner: Orchestrate discovery         │
└────────────────┬────────────────────────────────┘
                 │
                 │ APISubmitObserver
                 │ (batch mode)
                 ▼
┌─────────────────────────────────────────────────┐
│           API Client (api_client.py)             │
│  - HTTP client with retry logic                 │
│  - submit_batch() for efficiency                │
└────────────────┬────────────────────────────────┘
                 │
                 │ HTTP POST
                 ▼
┌─────────────────────────────────────────────────┐
│          API Server (api_server.py)              │
│  - FastAPI endpoints                            │
│  - Pydantic validation                          │
│  - Dependency injection                         │
└────────────────┬────────────────────────────────┘
                 │
                 │ SubmitModuleCommand
                 ▼
┌─────────────────────────────────────────────────┐
│          API Handler (api.py)                    │
│  - Command pattern: Submit/Health/Metrics       │
│  - Observer pattern: Logging/Metrics            │
│  - Strategy pattern: Queue backends             │
└────────────────┬────────────────────────────────┘
                 │
                 │ QueueStrategy.enqueue()
                 ▼
┌─────────────────────────────────────────────────┐
│              Queue (InMemoryQueue)               │
│  - asyncio.Queue with priority                  │
│  - Holds ModuleDiscoveryResult objects          │
│  - Ready for worker processing                  │
└─────────────────────────────────────────────────┘
                 │
                 │ [NEXT: Task 6]
                 ▼
┌─────────────────────────────────────────────────┐
│          Workers (workers.py - TODO)             │
│  - Async worker pool                            │
│  - Process queue items                          │
│  - Write to database                            │
└─────────────────────────────────────────────────┘
```

---

## Current Status

✅ **Tasks 1-5 Complete**:
- Configuration system
- Database models
- Module scanner
- API receiver
- Scanner API integration

🚧 **Next Task 6**: Async workers to process queue and write to database

📊 **Progress**: 5/19 tasks complete (26%)
