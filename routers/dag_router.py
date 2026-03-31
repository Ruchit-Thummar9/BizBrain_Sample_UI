from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Any

router = APIRouter()


class NodeData(BaseModel):
    id: str
    label: str
    type: str
    description: Optional[str] = None
    formula: Optional[str] = None
    value: Optional[Any] = None
    unit: Optional[str] = None
    source: Optional[str] = None


class EdgeData(BaseModel):
    id: str
    source: str
    target: str
    relation: Optional[str] = None


class NodeElement(BaseModel):
    data: NodeData


class EdgeElement(BaseModel):
    data: EdgeData


class AddNodeRequest(BaseModel):
    id: str
    label: str
    type: str
    description: Optional[str] = None
    formula: Optional[str] = None


class AddEdgeRequest(BaseModel):
    source: str
    target: str
    relation: str


class DeleteRequest(BaseModel):
    id: str


@router.get("/get")
def get_dag():
    try:
        raise NotImplementedError("DAG DB not yet connected. Plug in db.database.get_full_dag() here.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DAG load failed: {str(e)}")


@router.get("/nodes")
def get_nodes(node_type: Optional[str] = None):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/nodes/{node_id}")
def get_node(node_id: str):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/nodes")
def add_node(request: AddNodeRequest):
    if not request.id or not request.label:
        raise HTTPException(status_code=400, detail="id and label are required")

    valid_types = {"Atom", "Field", "Aterm", "Goal", "Operator", "Iterm"}
    if request.type not in valid_types:
        raise HTTPException(status_code=400, detail=f"type must be one of: {valid_types}")

    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/edges")
def add_edge(request: AddEdgeRequest):
    if not request.source or not request.target:
        raise HTTPException(status_code=400, detail="source and target are required")
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/nodes/{node_id}")
def delete_node(node_id: str):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats")
def dag_stats():
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status")
def dag_status():
    return JSONResponse({
        "service": "DAG",
        "status": "router_ok",
        "endpoints": [
            "GET  /api/dag/get",
            "GET  /api/dag/nodes",
            "GET  /api/dag/nodes/{node_id}",
            "POST /api/dag/nodes",
            "POST /api/dag/edges",
            "DELETE /api/dag/nodes/{node_id}",
            "GET  /api/dag/stats",
        ]
    })