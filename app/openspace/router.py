import json
from fastapi import APIRouter, HTTPException
from typing import Union

from app.openspace.main import (
    todays_date,
    astronomy_pic_of_day,
    where_is_iss
)

router = APIRouter()

@router.get("/apod/today")
async def apod_today():
    """NASA Astronomy picture of the day"""
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
    """Date Format : yyyy-mm-dd"""
    try:
        response = await astronomy_pic_of_day(date)
        return response

    except Exception as e:
        return {
            "message":"error",
            "error":str(e)
        }

@router.get("/iss")
async def iss_info():
    """Get the current position, velocity and altitude of ISS"""
    try:
        response = await where_is_iss()
        return response

    except Exception as e:
        return {
            "message":"error",
            "error":str(e)
        }