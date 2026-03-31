from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
from typing import Optional, List, Any

router = APIRouter()


class GoalRequest(BaseModel):
    goal: str

    @validator("goal")
    def goal_must_not_be_empty(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("goal cannot be empty")
        if len(v) > 500:
            raise ValueError("goal too long, max 500 characters")
        return v


class AtermResult(BaseModel):
    aterm_name: str
    formula: Optional[str] = None
    value: Any = None


class CompileResult(BaseModel):
    goal: str
    answer: Any
    aterm_name: Optional[str] = None
    aterms: Optional[List[AtermResult]] = None
    explanation: Optional[str] = None


class AtermSaveRequest(BaseModel):
    name: str
    formula: str
    value: Optional[Any] = None
    goal: Optional[str] = None


@router.post("/compile-goal", response_model=CompileResult)
def compile_goal(request: GoalRequest):
    try:
        raise NotImplementedError("Compiler service not yet connected. Plug in compiler_service.compile_goal_to_aterm() here.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Compilation failed: {str(e)}")


@router.get("/aterms")
def get_all_aterms():
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/aterms/{aterm_name}")
def get_aterm(aterm_name: str):
    if not aterm_name:
        raise HTTPException(status_code=400, detail="aterm_name is required")
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/aterms")
def save_aterm(request: AtermSaveRequest):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/aterms/{aterm_name}")
def delete_aterm(aterm_name: str):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status")
def compiler_status():
    return JSONResponse({
        "service": "GPL Compiler",
        "owner": "James",
        "status": "router_ok",
        "endpoints": [
            "POST /api/compiler/compile-goal",
            "GET  /api/compiler/aterms",
            "GET  /api/compiler/aterms/{aterm_name}",
            "POST /api/compiler/aterms",
            "DELETE /api/compiler/aterms/{aterm_name}",
        ]
    })