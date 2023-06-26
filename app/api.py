from fastapi import FastAPI
from app.imagine.router import router as ImagineRouter
from app.coderunner.router import router as CodeRunnerRouter
from app.sanatan.router import router as sanatanRouter

app = FastAPI(
		title="tg-api"
	)


# --------------------------------------------------------------------------
#                                Routers

app.include_router(ImagineRouter, prefix="/api/v1/imagine", tags=["imagine"])
app.include_router(CodeRunnerRouter, prefix="/api/v1/coderunner", tags=["coderunner"])
app.include_router(sanatanRouter, prefix="/api/v1/sanatan", tags=["sanatan"])

# --------------------------------------------------------------------------


@app.get("/", tags=["Root"])
async def read_root():
	return {
		"message": "Official @pyguru telegram api"
	}