from fastapi import APIRouter
from typing import Union
from loguru import logger
from fastapi.responses import Response

from app.model import ImagineRequest, ImageResponse
from app.imagegen.imagine import imagine
from app.imagegen.models import all_models
from app.imagegen.unstable import unstable_diffusion

router = APIRouter()


@router.post("/imagine")
async def imagine_engine(request: ImagineRequest) -> Union[ImageResponse, dict]:
    try:
        prompt = request.prompt
        model = request.model
        data = await imagine(prompt, model)

        return Response(
            content=data, media_type="image/png", headers={"prompt": prompt}
        )
    except Exception as e:
        return {"message": "error", "prompt": prompt, "content": None, "error": str(e)}


@router.get("/models")
async def models() -> dict:
    return {"message": "success", "models": await all_models()}


@router.post("/unstable")
async def unstable_engine(request: ImagineRequest) -> Union[ImageResponse, dict]:
    try:
        prompt = request.prompt
        model = request.model
        secret_key = request.secret_key

        data = await unstable_diffusion(prompt, model, secret_key)
        logger.info(f"{data=}")

        return Response(
            content=data, media_type="image/png", headers={"prompt": prompt}
        )
    except Exception as e:
        return {"message": "error", "prompt": prompt, "content": None, "error": str(e)}

