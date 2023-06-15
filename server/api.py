from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
	return {
		"message": "Official @pyguru telegram api"
	}