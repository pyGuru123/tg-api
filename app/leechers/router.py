from fastapi import APIRouter, HTTPException
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.model import libgenRequest, leechRequest
from app.leechers.libgen import scrape_libgen
from app.leechers.ytsmx import get_yts_magnet
from app.leechers.nyaasi import get_nyaasi_magnet
from app.leechers.zooqle import get_zooqle_magnet
from app.leechers._1337x import get_1337x_magnet
from app.leechers.magnetdl import get_magnetdl_magnet
from app.leechers.bitsearch import get_bitsearch_magnet
from app.leechers.piratesbay import get_piratesbay_magnet


router = APIRouter()


@router.post("/piratesbay")
async def piratesbay(request: leechRequest) -> list[dict]:
    """Get Magnet Links directly from piratesbay"""
    try:
        result = await get_piratesbay_magnet(request.movie)
        return result
    except Exception as e:
            raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.post("/ytsmx")
async def ytsmx(request: leechRequest) -> list[dict]:
    """Get Magnet Links directly from ytsmx"""
    try:
        result = await get_yts_magnet(request.movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.post("/1337x")
async def _1337x(request: leechRequest) -> list[dict]:
    """Get Magnet Links directly from 1337x.to"""
    try:
        result = await get_1337x_magnet(request.movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.post("/bitsearch")
async def bitsearch(request: leechRequest) -> list[dict]:
    """Get Magnet Links directly from bitsearch.to"""
    try:
        result = await get_bitsearch_magnet(request.movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.post("/magnetdl")
async def magnetdl(request: leechRequest) -> list[dict]:
    """Get Magnet Links directly from bitsearch.to"""
    try:
        result = await get_magnetdl_magnet(request.movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.post("/nyaasi")
async def nyaasi(request: leechRequest) -> list[dict]:
    """Get Magnet Links directly from nyaa.si"""
    try:
        result = await get_nyaasi_magnet(request.movie)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch magnets")

@router.post("/zooqle")
async def zooqle(request: leechRequest) -> list[dict]:
    """Get Magnet Links directly from zooqle.xyz"""
    try:
        result = await get_zooqle_magnet(request.movie)
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