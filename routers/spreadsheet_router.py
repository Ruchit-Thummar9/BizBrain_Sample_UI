from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
from typing import Optional, List, Any

router = APIRouter()


class SpreadsheetResult(BaseModel):
    sheet_id: str
    filename: str
    rows: Optional[int] = None
    columns: Optional[int] = None
    headers: Optional[List[str]] = None
    preview: Optional[List[dict]] = None


class QueryRequest(BaseModel):
    sheet_id: str
    query: str

    @validator("query")
    def query_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("query cannot be empty")
        return v.strip()


class QueryResult(BaseModel):
    sheet_id: str
    query: str
    result: Any
    rows_matched: Optional[int] = None


class ExportRequest(BaseModel):
    sheet_id: str
    format: str = "csv"

    @validator("format")
    def validate_format(cls, v):
        if v not in ("csv", "json"):
            raise ValueError("format must be 'csv' or 'json'")
        return v


@router.post("/upload", response_model=SpreadsheetResult)
def upload_spreadsheet(file: UploadFile = File(...)):
    allowed_exts = (".xlsx", ".xls", ".csv")

    ext = "." + file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in allowed_exts:
        raise HTTPException(status_code=400, detail="Only .xlsx, .xls, or .csv files accepted")

    contents = file.file.read()
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Empty file")
    if len(contents) > 20 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large. Max 20MB")

    try:
        raise NotImplementedError("Spreadsheet service not yet connected. Plug in spreadsheet_service.process_spreadsheet() here.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Spreadsheet processing failed: {str(e)}")


@router.post("/query", response_model=QueryResult)
def query_spreadsheet(request: QueryRequest):
    try:
        raise NotImplementedError("Spreadsheet query service not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sheets")
def get_all_sheets():
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sheets/{sheet_id}")
def get_sheet(sheet_id: str):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/sheets/{sheet_id}")
def delete_sheet(sheet_id: str):
    try:
        raise NotImplementedError("DB not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/export")
def export_sheet(request: ExportRequest):
    try:
        raise NotImplementedError("Export not yet connected.")
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status")
def spreadsheet_status():
    return JSONResponse({
        "service": "Spreadsheet",
        "owner": "Krutanshu",
        "status": "router_ok",
        "endpoints": [
            "POST /api/spreadsheet/upload",
            "POST /api/spreadsheet/query",
            "GET  /api/spreadsheet/sheets",
            "GET  /api/spreadsheet/sheets/{sheet_id}",
            "DELETE /api/spreadsheet/sheets/{sheet_id}",
            "POST /api/spreadsheet/export",
        ]
    })