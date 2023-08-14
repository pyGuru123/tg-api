from fastapi import APIRouter, UploadFile, File
from typing import Union
from loguru import logger

from app.model import SmmFakerRequest
from app.smmfaker.telegram import get_tg_views

router = APIRouter()


@router.post("/tg/views")
async def tg_views(request: SmmFakerRequest) -> dict:
    """Get Free Telegram Post Views : Max 1000 views per request"""
    try:
        post_url = request.post_url
        views = request.views
        status = await get_tg_views(post_url, views)

        return {"status": status, "error": ""}
    except Exception as e:
        return {"status": status, "error": str(e)}
