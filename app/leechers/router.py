from fastapi import APIRouter, HTTPException
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.leechers.piratesbay import get_piratesbay_magnets
from app.leechers.ytsmx import get_yts_magnet


router = APIRouter()


@router.get("/piratesbay/{movie}")
async def piratesbay(movie: str) -> list[dict]:
    """Get Magnet Links directly from piratesbay"""
    try:
        result = await get_piratesbay_magnets(movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.get("/ytsmx/{movie}")
async def ytsmx(movie: str) -> list[dict]:
    """Get Magnet Links directly from piratesbay"""
    try:
        result = await get_yts_magnet(movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")