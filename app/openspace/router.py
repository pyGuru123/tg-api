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

# @router.post("/epic")
# async def epic():
#     """The EPIC API provides information on the daily imagery collected by DSCOVR's Earth Polychromatic Imaging Camera (EPIC)
#      instrument. Uniquely positioned at the Earth-Sun Lagrange point, EPIC provides full disc imagery of the Earth and
#       captures unique perspectives of certain astronomical events such as lunar transits using a 
#       2048x2048 pixel CCD (Charge Coupled Device) detector coupled to a 30-cm aperture Cassegrain telescope."""