from fastapi import APIRouter, UploadFile, File
from typing import Union
from loguru import logger
from fastapi.responses import Response

from app.model import ImagineRequest, ImageResponse
from app.imageai.imagine import imagine, all_models
from app.imageai.unstable import unstable_diffusion
from app.imageai.colorizer import (
    colorize_picture,
    restore_picture
)


router = APIRouter()


@router.post("/imagine")
async def imagine_engine(request: ImagineRequest) -> Union[ImageResponse, dict]:
    """Generates image from text. Get models list from /models endpoint"""
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
    """Returns a list of endpoints that can be used with /imagine endpoint"""
    return {"message": "success", "models": await all_models()}


@router.post("/unstable")
async def unstable_engine(request: ImagineRequest) -> Union[ImageResponse, dict]:
    """Generate High Quality NSFW images, requires a secret key - get it from Author"""
    try:
        prompt = request.prompt
        model = request.model
        secret_key = request.secret_key

        data = await unstable_diffusion(prompt, model, secret_key)

        return Response(
            content=data, media_type="image/png", headers={"prompt": prompt}
        )
    except Exception as e:
        return {"message": "error", "prompt": prompt, "content": None, "error": str(e)}


@router.post("/colorize")
async def colorize_engine(file: UploadFile = File(...)) -> Union[ImageResponse, dict]:
    try:
        content = await file.read()
        filename = file.filename

        data = await colorize_picture(filename, content)

        return Response(
            content=data, media_type="image/png"
        )
    except Exception as e:
        return {"message": "error", "content": None, "error": str(e)}


@router.post("/restore")
async def restore_engine(file: UploadFile = File(...), withScratch: bool = File(...)) -> Union[ImageResponse, dict]:
    try:
        content = await file.read()
        filename = file.filename

        data = await restore_picture(filename, content, withScratch)

        return Response(
            content=data, media_type="image/png"
        )
    except Exception as e:
        return {"message": "error", "content": None, "error": str(e)}