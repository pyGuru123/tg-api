from fastapi import APIRouter, HTTPException
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.model import libgenRequest
from app.leechers.piratesbay import get_piratesbay_magnets
from app.leechers.ytsmx import get_yts_magnet
from app.leechers.libgen import scrape_libgen
from app.leechers.nyaasi import get_nyaasi_magnet


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

@router.get("/nyaasi/{movie}")
async def ytsmx(movie: str) -> list[dict]:
    """Get Magnet Links directly from nyaa.si"""
    try:
        result = await get_nyaasi_magnet(movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.post("/libgen")
async def libgen(request: libgenRequest) -> list[dict]:
    """Get PDF ebook download links directly from libgen"""
    try:
        if not (request.isbn or request.book_name):
            raise HTTPException(status_code=422, detail="Either 'isbn' or 'book_name' must be provided")

        query = str(request.isbn) or str(request.book_name).replace(" ", "+")
        result = await scrape_libgen(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch pdf links")