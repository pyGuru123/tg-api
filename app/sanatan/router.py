import json
from fastapi import APIRouter, HTTPException
from typing import Union

from app.model import sanatanResponse, ImageUrlResponse
from app.model import gitaRequest, gitaResponse
from app.sanatan.main import gitapress_data, todays_date
from app.sanatan.mahadev import get_mahadev_pic

router = APIRouter()

with open("app/sanatan/gita.json", "r") as gita_file:
    gita = json.load(gita_file)


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

@router.get("/gita/chapters")
async def chapters():
    return gita["chapters"]

@router.get("/gita/verse_count")
async def verse_count():
    return {
        int(chapter) : gita["chapters"][chapter]["verses_count"] for chapter in gita["chapters"]
    }

@router.post("/gita/verse")
async def verse(request: gitaRequest) -> gitaResponse:
    try:
        chapter = str(request.chapter)
        verse = str(request.verse)
        data = gita["verses"][chapter][verse]

        return gitaResponse(**data)
    except:
        raise HTTPException(status_code=404, detail="verse not found")
