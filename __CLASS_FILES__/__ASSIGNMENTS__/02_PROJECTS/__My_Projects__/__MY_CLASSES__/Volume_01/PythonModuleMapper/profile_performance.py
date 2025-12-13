import time
import cProfile
import pstats
import io
from pathlib import Path
from models import DatabaseSessionFactory
from graph import RelationshipGraphBuilder
from query import QueryInterface

def profile_operation(name, func, *args, **kwargs):
    """Run a function with profiling and print stats."""
    print(f"\n{'='*20} Profiling: {name} {'='*20}")
    
    pr = cProfile.Profile()
    pr.enable()
    
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    
    pr.disable()
    
    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    
    s = io.StringIO()
    sortby = pstats.SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats(20)  # Print top 20 cumulative time functions
    print(s.getvalue())
    
    return result

def run_benchmarks():
    db_path = "python_modules.db"
    if not Path(db_path).exists():
        print(f"Database {db_path} not found. Please run 'python cli.py populate' first.")
        return

    print(f"Connecting to {db_path}...")
    factory = DatabaseSessionFactory(f"sqlite:///{db_path}")
    
    # 1. Profile Graph Building
    # This might be fast if it just initializes, or slow if it loads everything.
    # Let's check graph.py implementation later, but for now we profile the init.
    graph = profile_operation("Graph Initialization", RelationshipGraphBuilder, factory)
    
    # 2. Profile Search
    query = QueryInterface(graph)
    profile_operation("Search 'json'", query.search_by_name, "json")
    
    # 3. Profile Dependency Traversal
    # We need a module that likely exists. 'json' or 'os' are good candidates.
    # We'll try to find a node first to ensure it exists.
    results = query.search_by_name("json")
    if results.results:
        node_name = results.results[0].name
        print(f"Analyzing dependencies for: {node_name}")
        profile_operation(f"Get Dependencies ({node_name}) - Run 1", graph.find_dependencies, node_name)
        profile_operation(f"Get Dependencies ({node_name}) - Run 2 (Cached)", graph.find_dependencies, node_name)
    else:
        print("Could not find 'json' module to test dependencies.")

    # 4. Profile Complex Query (if applicable)
    # For example, finding all classes in a module
    profile_operation("Search 'Module' type", query.search_by_type, "module")

if __name__ == "__main__":
    run_benchmarks()
