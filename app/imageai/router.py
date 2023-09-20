from fastapi import APIRouter, UploadFile, File
from typing import Union
from loguru import logger
from fastapi.responses import Response

from app.model import ImagineRequest, ImageResponse
from app.imageai.imagine import imagine_art, imagine_all_models
from app.imageai.prodia import imagine_prodia, prodia_all_models
from app.imageai.unstable import unstable_diffusion, unstable_all_models
from app.imageai.artmaker import art_maker, artmaker_all_models

router = APIRouter()

@router.post("/imagine")
async def imagine_engine(request: ImagineRequest) -> Union[ImageResponse, dict]:
    """Generates image from text. Get models list from /models endpoint"""
    # try:
    prompt = request.prompt
    model = request.model
    data = await imagine_art(prompt, model)

    return Response(
        content=data, media_type="image/png", headers={"prompt": prompt}
    )
    # except Exception as e:
    #     return {"message": "error", "prompt": prompt, "content": None, "error": str(e)}


@router.get("/imagine/models")
async def imagine_models() -> dict:
    """Returns a list of models that can be used with /prodia endpoint"""
    return {"message": "success", "models": await imagine_all_models()}

@router.post("/prodia")
async def prodia_engine(request: ImagineRequest) -> Union[ImageResponse, dict]:
    """Generates image from text. Get models list from /models endpoint"""
    try:
        prompt = request.prompt
        model = request.model
        data = await imagine_prodia(prompt, model)

        return Response(
            content=data, media_type="image/png", headers={"prompt": prompt}
        )
    except Exception as e:
        return {"message": "error", "prompt": prompt, "content": None, "error": str(e)}


@router.get("/prodia/models")
async def prodia_models() -> dict:
    """Returns a list of models that can be used with /prodia endpoint"""
    return {"message": "success", "models": await prodia_all_models()}


@router.post("/artmaker")
async def artmaker_engine(request: ImagineRequest) -> Union[ImageResponse, dict]:
    """Generate High Quality images using multiple models"""
    try:
        prompt = request.prompt
        model = request.model

        data = await art_maker(prompt, model)

        return Response(
            content=data, media_type="image/png", headers={"prompt": prompt}
        )
    except Exception as e:
        return {"message": "error", "prompt": prompt, "content": None, "error": str(e)}


@router.get("/artmaker/models")
async def artmaker_models() -> dict:
    """Returns a list of models that can be used with /imagine endpoint"""
    return {"message": "success", "models": await artmaker_all_models()}


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


@router.get("/unstable/models")
async def unstable_models() -> dict:
    """Returns a list of models that can be used with /unstable endpoint"""
    return {"message": "success", "models": await unstable_all_models()}
