from fastapi import APIRouter, HTTPException
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.model import leechRequest
from app.gdtot.cinevood import get_cinevood_links


router = APIRouter()


@router.post("/cinevood")
async def piratesbay(request: leechRequest) -> list[dict]:
    """Get GDTOT Links directly from cinevood"""
    try:
        result = await get_cinevood_links(request.movie)
        return result
    except Exception as e:
            raise HTTPException(status_code=404, detail="Unable to fetch magnets")

