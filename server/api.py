from fastapi import FastAPI
from server.imagine_route import router as ImagineRouter

app = FastAPI()
app.include_router(ImagineRouter, prefix="/about")

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