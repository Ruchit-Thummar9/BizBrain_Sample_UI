from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import os

router = APIRouter()


class DocumentResult(BaseModel):
    doc_id: str
    filename: str
    vendor: Optional[str] = None
    doc_type: Optional[str] = None
    amount: Optional[float] = None
    tax: Optional[float] = None
    date: Optional[str] = None
    currency: Optional[str] = "USD"
    raw_text: Optional[str] = None


class DeleteRequest(BaseModel):
    doc_id: str


@router.post("/upload-document", response_model=DocumentResult)
def upload_document(file: UploadFile = File(...)):
    if file.content_type not in ("application/pdf", "application/octet-stream"):
        raise HTTPException(status_code=400, detail="PDF files only")

    contents = file.file.read()
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large. Max 10MB")

    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Empty file")

    try:
        raise NotImplementedError("SOT service not yet connected. Plug in sot_service.process_document() here.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SOT processing failed: {str(e)}")


@router.get("/documents")
def get_all_documents():
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/documents/{doc_id}")
def get_document(doc_id: str):
    if not doc_id:
        raise HTTPException(status_code=400, detail="doc_id is required")
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/documents/{doc_id}")
def delete_document(doc_id: str):
    if not doc_id:
        raise HTTPException(status_code=400, detail="doc_id is required")
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status")
def sot_status():
    return JSONResponse({
        "service": "SOT",
        "owner": "Ritik",
        "status": "router_ok",
        "endpoints": [
            "POST /api/sot/upload-document",
            "GET  /api/sot/documents",
            "GET  /api/sot/documents/{doc_id}",
            "DELETE /api/sot/documents/{doc_id}",
        ]
    })