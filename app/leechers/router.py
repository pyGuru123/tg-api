from fastapi import APIRouter, HTTPException
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.leechers.piratesbay import get_magnets


router = APIRouter()


@router.get("/piratesbay/{movie}")
async def piratesbay(movie: str) -> list[dict]:
    """Get Magnet Links directly from piratesbay"""
    try:
        result = await get_magnets(movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, details="Unable to fetch magnets")