import json
from fastapi import APIRouter, HTTPException
from typing import Union

from app.openspace.main import (
    todays_date,
    astronomy_pic_of_day
)

router = APIRouter()

@router.get("/apod/today")
async def apod_today():
    try:
        date = todays_date()
        response = await astronomy_pic_of_day(date)
        return response
    except Exception as e:
        return {
            "message":"error",
            "error":str(e)
        }

@router.get("/apod/date")
async def apod(date):
    try:
        response = await astronomy_pic_of_day(date)
        return response

    except Exception as e:
        return {
            "message":"error",
            "error":str(e)
        }
