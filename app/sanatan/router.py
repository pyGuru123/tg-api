from fastapi import APIRouter
from typing import Union

from app.model import sanatanResponse, ImageUrlResponse
from app.sanatan.main import gitapress_data, todays_date
from app.sanatan.mahadev import get_mahadev_pic

router = APIRouter()


@router.get("/today")
async def today() -> sanatanResponse:
    try:
        todays_data = await gitapress_data()
        response = sanatanResponse(**todays_data)

        return response

    except Exception as e:
        return sanatanResponse(
            message="error",
            error=str(e),
            date=todays_date(),
            sunrise="",
            sunset="",
            shloka="",
            importance="",
        )

@router.get("/mahadev")
async def mahadev() -> ImageUrlResponse:
    url = get_mahadev_pic()
    return ImageUrlResponse(
        url=url
    )
