# Quick Start Guide - Module Discovery API

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Running the API Server

```bash
# Option 1: Using Python directly
python api_server.py

# Option 2: Using uvicorn
uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: `http://localhost:8000`

## API Documentation

Interactive API docs available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing the API

### Option 1: Run Test Suite
```bash
# Terminal 1: Start server
python api_server.py

# Terminal 2: Run tests
python test_api.py
```

### Option 2: Manual Testing with curl

**Health Check:**
```bash
curl http://localhost:8000/api/v1/health
```

**Submit Module:**
```bash
curl -X POST http://localhost:8000/api/v1/modules \
  -H "Content-Type: application/json" \
  -d '{
    "module_name": "collections",
    "filepath": "/usr/lib/python3.9/collections.py",
    "is_package": false,
    "classes": [{"name": "OrderedDict", "lineno": 100}],
    "functions": [{"name": "namedtuple", "lineno": 50}],
    "imports": ["sys", "_collections"],
    "checksum": "abc123",
    "scanner_version": "1.0.0"
  }'
```

**Get Metrics:**
```bash
curl http://localhost:8000/api/v1/metrics
```

### Option 3: Python Client
```python
from api_client import APIClient
from datetime import datetime

client = APIClient(base_url="http://localhost:8000")

# Submit module
result = client.submit_module({
    'module_name': 'test_module',
    'filepath': '/path/to/module.py',
    'is_package': False,
    'classes': [],
    'functions': [{'name': 'test_func', 'lineno': 10}],
    'imports': ['sys'],
    'checksum': 'test123',
    'discovered_at': datetime.utcnow().isoformat(),
    'scanner_version': '1.0.0'
})

print(f"Queue ID: {result['queue_id']}")

# Check health
health = client.health_check()
print(f"Status: {health['status']}")

client.close()
```

## Project Structure

```
PythonModuleMapper/
├── api.py              # Core API handler (Command/Observer/Strategy)
├── api_server.py       # FastAPI REST wrapper
├── api_client.py       # HTTP client for scanner
├── config.py           # Configuration (Builder/Strategy)
├── models.py           # Database models (Repository/UoW/Factory)
├── scanner.py          # Module scanner (Command/Observer)
├── test_api.py         # API test suite
├── requirements.txt    # Dependencies
├── ENTRYPOINT.txt      # Iteration protocol
├── DASHBOARD.md        # Project overview
├── ARCHITECTURE.md     # System architecture
├── tasks.csv           # Task tracking
└── TASK_4_SUMMARY.md   # Current task summary
```

## Next Steps

1. **Task 5**: Integrate scanner.py with API client
2. **Task 6**: Build async workers to process queue
3. **Task 7**: Write processed data to database

## Troubleshooting

**Port already in use:**
```bash
# Change port in api_server.py or use:
uvicorn api_server:app --port 8001
```

**Module import errors:**
```bash
# Ensure you're in the project directory
cd PythonModuleMapper
python api_server.py
```

**Dependencies missing:**
```bash
pip install -r requirements.txt
```

## Configuration

Default configuration (can be customized in `api_server.py`):
- Queue capacity: 1000 items
- Observers: LoggingObserver, MetricsObserver
- Queue backend: InMemoryQueueStrategy (asyncio.Queue)

To use Redis queue backend (future):
```python
from redis_queue import RedisQueueStrategy

queue_strategy = RedisQueueStrategy(
    host='localhost',
    port=6379,
    max_size=1000
)
```

## Resources

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Pydantic**: https://docs.pydantic.dev/
- **Design Patterns**: See `UNIFIED_PATTERNS/` directory
