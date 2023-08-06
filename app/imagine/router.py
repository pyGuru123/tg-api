from fastapi import APIRouter
from typing import Union
from fastapi.responses import Response

from app.model import ImagineRequest, ImageResponse
from app.imagine.main import imagine
from app.imagine.models import all_models

router = APIRouter()


@router.post("/generate")
async def generate(request: ImagineRequest) -> Union[ImageResponse, dict]:
    try:
        prompt = request.prompt
        model = request.model
        upscale = request.upscale
        data = await imagine(prompt, model, upscale)

        return Response(
            content=data, media_type="image/png", headers={"prompt": prompt}
        )
    except Exception as e:
        return {"message": "error", "prompt": prompt, "content": None, "error": str(e)}


@router.get("/models")
async def models() -> dict:
    return {"message": "success", "models": await all_models()}
