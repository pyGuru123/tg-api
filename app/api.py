from fastapi import FastAPI
from app.imagine.router import router as ImagineRouter

from imaginepy import Imagine

app = FastAPI(
		title="tg-api"
	)

# @app.on_event("startup")
# async def startup():
# 	app.imagine = Imagine()


# --------------------------------------------------------------------------
#                                Routers

app.include_router(ImagineRouter, prefix="/api/v1/imagine", tags=["Imagine"])

# --------------------------------------------------------------------------


@app.get("/", tags=["Root"])
async def read_root():
	return {
		"message": "Official @pyguru telegram api"
	}

@app.get("/about", tags=["Root"])
async def about():
	return {
		"message": "This api is created by @itspyguru"
	}