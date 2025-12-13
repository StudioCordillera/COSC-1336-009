"""
FastAPI REST API Wrapper for Module Discovery System

Exposes APIEndpointHandler commands via HTTP endpoints.
Uses dependency injection for all components.

Installation:
    pip install fastapi uvicorn

Run:
    uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload
"""

from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from datetime import datetime
import uvicorn

from api import (
    APIEndpointHandler,
    QueueStrategy,
    InMemoryQueueStrategy,
    QueueObserver,
    LoggingObserver,
    MetricsObserver,
    ModuleDiscoveryResult
)
from models import DatabaseSessionFactory
from graph import RelationshipGraphBuilder


# ============================================================================
# Pydantic Models for Request/Response Validation
# ============================================================================

class ModuleSubmissionRequest(BaseModel):
    """Request model for module submission"""
    module_name: str = Field(..., description="Name of the Python module")
    filepath: str = Field(..., description="Absolute path to the module file")
    is_package: bool = Field(False, description="Whether this is a package")
    classes: list[Dict[str, Any]] = Field(default_factory=list, description="List of classes found")
    functions: list[Dict[str, Any]] = Field(default_factory=list, description="List of functions found")
    imports: list[str] = Field(default_factory=list, description="List of imports")
    checksum: str = Field(..., description="File checksum (MD5/SHA256)")
    discovered_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat(), description="Discovery timestamp")
    scanner_version: str = Field("1.0.0", description="Scanner version")
    
    class Config:
        schema_extra = {
            "example": {
                "module_name": "collections",
                "filepath": "/usr/lib/python3.9/collections.py",
                "is_package": False,
                "classes": [
                    {"name": "OrderedDict", "lineno": 100, "methods": ["__init__", "update"]}
                ],
                "functions": [
                    {"name": "namedtuple", "lineno": 50, "params": ["typename", "field_names"]}
                ],
                "imports": ["sys", "_collections"],
                "checksum": "a1b2c3d4e5f6",
                "discovered_at": "2025-12-09T12:00:00",
                "scanner_version": "1.0.0"
            }
        }


class ModuleSubmissionResponse(BaseModel):
    """Response model for module submission"""
    status: str
    queue_id: Optional[str] = None
    module: str
    timestamp: str
    error: Optional[str] = None


class HealthCheckResponse(BaseModel):
    """Response model for health check"""
    status: str
    timestamp: str
    queue: Dict[str, Any]
    database: str


class MetricsResponse(BaseModel):
    """Response model for metrics"""
    timestamp: str
    queue: Dict[str, Any]
    processing: Optional[Dict[str, Any]] = None


# ============================================================================
# Dependency Injection Setup
# ============================================================================

class APIConfiguration:
    """
    Configuration container for API dependencies.
    Uses dependency injection pattern.
    """
    
    def __init__(
        self,
        queue_strategy: QueueStrategy,
        observers: list[QueueObserver],
        db_factory: Any = None,
        graph_builder: Any = None
    ):
        self.queue_strategy = queue_strategy
        self.observers = observers
        self.db_factory = db_factory
        self.graph_builder = graph_builder
        
        # Create handler with injected dependencies
        self.handler = APIEndpointHandler(
            queue_strategy=self.queue_strategy,
            observers=self.observers,
            db_factory=self.db_factory
        )


# Global configuration (initialized in lifespan)
api_config: Optional[APIConfiguration] = None


def get_api_handler() -> APIEndpointHandler:
    """Dependency function to get API handler"""
    if api_config is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="API not initialized"
        )
    return api_config.handler


def get_graph_builder() -> RelationshipGraphBuilder:
    """Dependency function to get Graph Builder"""
    if api_config is None or api_config.graph_builder is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Graph Builder not initialized"
        )
    return api_config.graph_builder


# ============================================================================
# FastAPI Application
# ============================================================================

app = FastAPI(
    title="Module Discovery API",
    description="REST API for Python module discovery and queuing system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Mount static files for dashboard
app.mount("/dashboard", StaticFiles(directory="dashboard", html=True), name="dashboard")


@app.on_event("startup")
async def startup_event():
    """Initialize API configuration on startup"""
    global api_config
    
    # Print all registered routes for debugging
    print("🛣️  Registered Routes:")
    for route in app.routes:
        print(f"   - {route.path} [{route.name}]")
    
    # Setup queue strategy
    queue_strategy = InMemoryQueueStrategy(maxsize=1000)
    
    # Setup observers
    observers = [
        LoggingObserver(),  # Console logging
        MetricsObserver()   # Metrics collection
    ]
    
    # Initialize database factory
    # Using local SQLite database for now
    db_factory = DatabaseSessionFactory("sqlite:///python_modules.db")
    
    # Initialize graph builder
    graph_builder = RelationshipGraphBuilder(db_factory)
    
    # Initialize configuration
    api_config = APIConfiguration(
        queue_strategy=queue_strategy,
        observers=observers,
        db_factory=db_factory,
        graph_builder=graph_builder
    )
    
    print("✅ Module Discovery API started")
    print("📊 Queue capacity: 1000 items")
    print("👀 Observers: LoggingObserver, MetricsObserver")
    print("🕸️  Graph Builder initialized")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print("🛑 Module Discovery API shutting down")


# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "service": "Module Discovery API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "submit": "POST /api/v1/modules",
            "health": "GET /api/v1/health",
            "metrics": "GET /api/v1/metrics",
            "docs": "GET /docs"
        }
    }


@app.post(
    "/api/v1/modules",
    response_model=ModuleSubmissionResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Modules"]
)
async def submit_module(
    request: ModuleSubmissionRequest,
    handler: APIEndpointHandler = Depends(get_api_handler)
):
    """
    Submit a discovered module to the processing queue.
    
    This endpoint accepts module discovery results and adds them to the queue
    for asynchronous processing. Each submission receives a unique queue ID
    for tracking.
    
    Returns:
        ModuleSubmissionResponse with queue_id and status
    """
    try:
        result = handler.submit_module(request.dict())
        
        if result['status'] == 'error':
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=result.get('error', 'Unknown error')
            )
        
        return ModuleSubmissionResponse(**result)
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@app.get(
    "/api/v1/health",
    response_model=HealthCheckResponse,
    tags=["System"]
)
async def health_check(
    handler: APIEndpointHandler = Depends(get_api_handler)
):
    """
    Check system health status.
    
    Returns current status of queue and database connectivity.
    """
    result = handler.health_check()
    return HealthCheckResponse(**result)


@app.get(
    "/api/v1/metrics",
    response_model=MetricsResponse,
    tags=["System"]
)
async def get_metrics(
    handler: APIEndpointHandler = Depends(get_api_handler)
):
    """
    Get system metrics.
    
    Returns statistics about queue usage and processing.
    """
    result = handler.get_metrics()
    return MetricsResponse(**result)


@app.post(
    "/api/v1/undo",
    tags=["Operations"]
)
async def undo_last_operation(
    handler: APIEndpointHandler = Depends(get_api_handler)
):
    """
    Undo the last successful operation.
    
    Attempts to remove the last submitted module from the queue.
    Only works if the module hasn't been processed yet.
    """
    result = handler.undo_last()
    
    if result['status'] == 'error':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result.get('error', 'Cannot undo')
        )
    
    return result


# ============================================================================
# Graph Visualization Endpoints
# ============================================================================

@app.get("/api/graph/data", tags=["Graph"])
async def get_graph_data(
    builder: RelationshipGraphBuilder = Depends(get_graph_builder)
):
    """
    Get full graph data for visualization.
    
    Returns:
        List of graph elements (nodes and edges) in Cytoscape.js format.
    """
    return builder.get_full_graph()


@app.get("/api/graph/search", tags=["Graph"])
async def search_graph(
    q: str,
    builder: RelationshipGraphBuilder = Depends(get_graph_builder)
):
    """
    Search graph nodes.
    
    Args:
        q: Search query string
        
    Returns:
        List of matching nodes and their immediate connections.
    """
    return builder.search_graph(q)


@app.get("/view/dashboard", response_class=HTMLResponse, tags=["Visualization"])
async def view_dashboard():
    """
    Serve dashboard HTML page.
    """
    with open("dashboard/index.html", "r") as f:
        return f.read()


# ============================================================================
# Example Client Code (for testing)
# ============================================================================

if __name__ == '__main__':
    """
    Run the API server.
    
    Usage:
        python api_server.py
    
    Or with uvicorn directly:
        uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload
    """
    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=5555,
        reload=True,
        log_level="info"
    )
