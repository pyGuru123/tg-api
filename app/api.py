from fastapi import FastAPI
from app.imagine.router import router as ImagineRouter

app = FastAPI(
		title="tg-api"
	)

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