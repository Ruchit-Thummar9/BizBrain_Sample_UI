from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
from typing import Optional, List

router = APIRouter()


class DocumentMeta(BaseModel):
    doc_id: str
    filename: str
    doc_type: Optional[str] = None
    page_count: Optional[int] = None
    size_kb: Optional[float] = None
    raw_text: Optional[str] = None
    summary: Optional[str] = None
    tags: Optional[List[str]] = None


class SearchRequest(BaseModel):
    query: str
    doc_type: Optional[str] = None
    limit: int = 10

    @validator("query")
    def query_not_empty(cls, v):
        if not v.strip():
            raise ValueError("query cannot be empty")
        return v.strip()

    @validator("limit")
    def limit_range(cls, v):
        if v < 1 or v > 100:
            raise ValueError("limit must be between 1 and 100")
        return v


class SummaryRequest(BaseModel):
    doc_id: str
    style: str = "brief"

    @validator("style")
    def validate_style(cls, v):
        if v not in ("brief", "detailed", "bullet_points"):
            raise ValueError("style must be brief, detailed, or bullet_points")
        return v


class TagRequest(BaseModel):
    doc_id: str
    tags: List[str]


@router.post("/load", response_model=DocumentMeta)
def load_document(file: UploadFile = File(...)):
    allowed_exts = (".pdf", ".docx", ".txt", ".doc")
    ext = "." + file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""

    if ext not in allowed_exts:
        raise HTTPException(status_code=400, detail="Only PDF, DOCX, or TXT files accepted")

    contents = file.file.read()
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Empty file")
    if len(contents) > 25 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large. Max 25MB")

    try:
        raise NotImplementedError("Documents service not yet connected. Plug in documents_service.load_document() here.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Document loading failed: {str(e)}")


@router.post("/search")
def search_documents(request: SearchRequest):
    try:
        raise NotImplementedError("Search service not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/summarise")
def summarise_document(request: SummaryRequest):
    try:
        raise NotImplementedError("Summarise service not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/raw-docs")
def get_all_raw_docs(
    doc_type: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=200)
):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/raw-docs/{doc_id}")
def get_raw_doc(doc_id: str):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/tag")
def tag_document(request: TagRequest):
    if not request.tags:
        raise HTTPException(status_code=400, detail="At least one tag required")
    try:
        raise NotImplementedError("Tagging not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/raw-docs/{doc_id}")
def delete_raw_doc(doc_id: str):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status")
def documents_status():
    return JSONResponse({
        "service": "Documents",
        "owner": "Krupal",
        "status": "router_ok",
        "endpoints": [
            "POST /api/documents/load",
            "POST /api/documents/search",
            "POST /api/documents/summarise",
            "POST /api/documents/tag",
            "GET  /api/documents/raw-docs",
            "GET  /api/documents/raw-docs/{doc_id}",
            "DELETE /api/documents/raw-docs/{doc_id}",
        ]
    })