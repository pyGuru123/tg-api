from fastapi import FastAPI
from app.imagine.router import router as ImagineRouter
from app.nhentai.router import router as nHentaiRouter

from imaginepy import Imagine

app = FastAPI(
		title="tg-api"
	)


# --------------------------------------------------------------------------
#                                Routers

app.include_router(ImagineRouter, prefix="/api/v1/imagine", tags=["imagine"])
app.include_router(nHentaiRouter, prefix="/api/v1/nhentai", tags=["nhentai"])

# --------------------------------------------------------------------------


@app.get("/", tags=["Root"])
async def read_root():
	return {
		"message": "Official @pyguru telegram api"
	}