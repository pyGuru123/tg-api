from fastapi import APIRouter, UploadFile, File
from typing import Union
from loguru import logger
from fastapi.responses import Response

from app.model import ImagineRequest, ImageResponse
from app.photorai.main import (
    colorize_picture,
    restore_picture,
    remove_background,
    upscale_image
)


router = APIRouter()

@router.post("/colorize")
async def colorize_engine(file: UploadFile = File(...)) -> Union[ImageResponse, dict]:
    """Colorize old black & white photos with this ai tool seamlessly"""
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
    """Restore old images, remove scratches from them using this ai tool"""
    try:
        content = await file.read()
        filename = file.filename

        data = await restore_picture(filename, content, withScratch)

        return Response(
            content=data, media_type="image/png"
        )
    except Exception as e:
        return {"message": "error", "content": None, "error": str(e)}

@router.post("/removebg")
async def removebg_engine(file: UploadFile = File(...)) -> Union[ImageResponse, dict]:
    """Remove background from images seamlessly with this ai tool"""
    try:
        content = await file.read()
        data = await remove_background(content)

        return Response(
            content=data, media_type="image/png"
        )
    except Exception as e:
        return {"message": "error", "content": None, "error": str(e)}

@router.post("/upscale")
async def upscale_engine(file: UploadFile = File(...)) -> Union[ImageResponse, dict]:
    """Remove background from images seamlessly with this ai tool"""
    try:
        content = await file.read()
        data = await upscale_image(content)

        return Response(
            content=data, media_type="image/png"
        )
    except Exception as e:
        return {"message": "error", "content": None, "error": str(e)}