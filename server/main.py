from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import os

from routers.sot_router         import router as sot_router
from routers.compiler_router    import router as compiler_router
from routers.spreadsheet_router import router as spreadsheet_router
from routers.documents_router   import router as documents_router
from routers.dag_router         import router as dag_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs("data/sot/documents", exist_ok=True)
    os.makedirs("data/bizbrain", exist_ok=True)
    yield


app = FastAPI(
    title="BizBrain 3",
    version="3.0.0",
    lifespan=lifespan,
)

app.include_router(sot_router,         prefix="/api/sot",         tags=["SOT"])
app.include_router(compiler_router,    prefix="/api/compiler",    tags=["Compiler"])
app.include_router(spreadsheet_router, prefix="/api/spreadsheet", tags=["Spreadsheet"])
app.include_router(documents_router,   prefix="/api/documents",   tags=["Documents"])
app.include_router(dag_router,         prefix="/api/dag",         tags=["DAG"])


@app.get("/api/health")
def health():
    return JSONResponse({"status": "ok", "version": "3.0.0"})


app.mount("/", StaticFiles(directory="static", html=True), name="static")