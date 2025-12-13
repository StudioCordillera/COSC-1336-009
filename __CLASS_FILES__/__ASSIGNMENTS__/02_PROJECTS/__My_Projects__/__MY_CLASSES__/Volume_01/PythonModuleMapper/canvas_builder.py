"""
Obsidian Canvas Builder

Generates .canvas JSON files for visualizing relationships in Obsidian.
Supports nodes (files, text, groups) and edges.
"""

import json
import uuid
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any

@dataclass
class CanvasNode:
    id: str
    x: int
    y: int
    width: int
    height: int
    type: str = "file"  # 'file', 'text', 'group'
    file: Optional[str] = None
    text: Optional[str] = None
    color: Optional[str] = None

@dataclass
class CanvasEdge:
    id: str
    fromNode: str
    fromSide: str  # 'top', 'bottom', 'left', 'right'
    toNode: str
    toSide: str
    color: Optional[str] = None
    label: Optional[str] = None

class CanvasBuilder:
    """Builder for Obsidian Canvas files"""
    
    def __init__(self):
        self.nodes: List[Dict[str, Any]] = []
        self.edges: List[Dict[str, Any]] = []
        self.node_map: Dict[str, str] = {}  # Map entity ID/name to node ID
        
    def add_file_node(self, file_path: str, x: int, y: int, width: int = 400, height: int = 400, color: str = None) -> str:
        """Add a file node to the canvas"""
        node_id = str(uuid.uuid4())
        node = {
            "id": node_id,
            "type": "file",
            "file": file_path,
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }
        if color:
            node["color"] = color
            
        self.nodes.append(node)
        self.node_map[file_path] = node_id
        return node_id

    def add_text_node(self, text: str, x: int, y: int, width: int = 400, height: int = 200, color: str = None) -> str:
        """Add a text node to the canvas"""
        node_id = str(uuid.uuid4())
        node = {
            "id": node_id,
            "type": "text",
            "text": text,
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }
        if color:
            node["color"] = color
            
        self.nodes.append(node)
        return node_id

    def add_edge(self, from_node_id: str, to_node_id: str, from_side: str = 'right', to_side: str = 'left', color: str = None, label: str = None):
        """Add an edge between nodes"""
        edge_id = str(uuid.uuid4())
        edge = {
            "id": edge_id,
            "fromNode": from_node_id,
            "fromSide": from_side,
            "toNode": to_node_id,
            "toSide": to_side
        }
        if color:
            edge["color"] = color
        if label:
            edge["label"] = label
            
        self.edges.append(edge)

    def get_node_id(self, key: str) -> Optional[str]:
        """Get node ID by key (e.g., file path)"""
        return self.node_map.get(key)

    def to_json(self) -> str:
        """Generate JSON string"""
        return json.dumps({
            "nodes": self.nodes,
            "edges": self.edges
        }, indent=2)

class CanvasLayout:
    """Helper for laying out nodes"""
    
    @staticmethod
    def grid(items: List[Any], cols: int = 5, start_x: int = 0, start_y: int = 0, 
             cell_width: int = 450, cell_height: int = 450) -> List[Dict[str, int]]:
        """Calculate grid positions for a list of items"""
        positions = []
        for i, item in enumerate(items):
            row = i // cols
            col = i % cols
            positions.append({
                "x": start_x + (col * cell_width),
                "y": start_y + (row * cell_height)
            })
        return positions

    @staticmethod
    def circle(center_x: int, center_y: int, radius: int, count: int) -> List[Dict[str, int]]:
        """Calculate circular positions"""
        import math
        positions = []
        if count == 0:
            return positions
            
        angle_step = (2 * math.pi) / count
        for i in range(count):
            angle = i * angle_step
            positions.append({
                "x": int(center_x + radius * math.cos(angle)),
                "y": int(center_y + radius * math.sin(angle))
            })
        return positions
