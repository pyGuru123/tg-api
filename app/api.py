from fastapi import FastAPI
from app.imagine.router import router as ImagineRouter
from app.nhentai.router import router as nHentaiRouter
from app.coderunner.router import router as CodeRunnerRouter

app = FastAPI(
		title="tg-api"
	)


# --------------------------------------------------------------------------
#                                Routers

app.include_router(ImagineRouter, prefix="/api/v1/imagine", tags=["imagine"])
app.include_router(nHentaiRouter, prefix="/api/v1/nhentai", tags=["nhentai"])
app.include_router(CodeRunnerRouter, prefix="/api/v1/coderunner", tags=["coderunner"])

# --------------------------------------------------------------------------


@app.get("/", tags=["Root"])
async def read_root():
	return {
		"message": "Official @pyguru telegram api"
	}