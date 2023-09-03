from fastapi import APIRouter, HTTPException
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.leechers.piratesbay import get_piratesbay_magnets
from app.leechers.ytsmx import get_yts_magnet
from app.leechers.libgen import scrape_libgen


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
    """Get Magnet Links directly from ytsmx"""
    try:
        result = await get_yts_magnet(movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.get("/libgen/{isbn}")
async def libgen(isbn: str) -> list[dict]:
    """Get PDF ebook download links directly from libgen"""
    try:
        isbn = str(isbn).replace(" ", "+")
        result = await scrape_libgen(isbn)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch pdf links")