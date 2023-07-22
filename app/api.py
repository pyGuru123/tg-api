from fastapi import FastAPI
from loguru import logger

from app.imagine.router import router as ImagineRouter
from app.coderunner.router import router as CodeRunnerRouter
from app.sanatan.router import router as SanatanRouter
from app.llmodels.router import router as LLMRouter
from app.search.router import router as SearchRouter

from app.llmodels.bard import session

app = FastAPI(title="tg-api")


# --------------------------------------------------------------------------
#                                Routers

app.include_router(ImagineRouter, prefix="/api/v1/imagine", tags=["imagine"])
app.include_router(LLMRouter, prefix="/api/v1/llmodels", tags=["llmodel"])
app.include_router(CodeRunnerRouter, prefix="/api/v1/coderunner", tags=["coderunner"])
app.include_router(SearchRouter, prefix="/api/v1/search", tags=["search"])
app.include_router(SanatanRouter, prefix="/api/v1/sanatan", tags=["sanatan"])

# --------------------------------------------------------------------------


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Official @pyguru telegram api"}


@app.on_event("shutdown")
def shutdown_event():
    logger.info("Application is shutting down")
    session.close()
    logger.info("Application shutdown successfully")
