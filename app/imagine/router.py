from fastapi import APIRouter
from fastapi.responses import Response
from pydantic import BaseModel

from app.imagine.main import imagine, all_styles

router = APIRouter()

class ImageRequest(BaseModel):
    prompt: str
    style: str

@router.post("/imagine")
async def imagineImg(request: ImageRequest):
	try:
		prompt = request.prompt
		style = request.style
		data = await imagine(prompt, style)
		return Response(content=data, media_type="image/png", headers={"prompt": prompt})
	except:
		return {"message" : "error", "prompt": prompt, "content": None}


@router.get("/styles")
async def styles():
	return {
		"message": "success",
		"styles": await all_styles()
	}