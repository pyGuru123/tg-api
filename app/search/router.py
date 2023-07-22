from fastapi import APIRouter
from typing import Union

from app.model import simpleRequest, simpleResponse
from app.search.main import search_wikipedia

router = APIRouter()


@router.post("/wiki")
async def wiki(request: simpleRequest) -> simpleResponse:
    """Search Wikipedia. Just enter search term and get a summary of the search term"""
    try:
        query = request.query
        data = search_wikipedia(query)

        return simpleResponse(
            message="success",
            query=query,
            content=data,
            error="",
        )
    except Exception as e:
        return simpleResponse(
            message="error",
            query=query,
            content="",
            error=str(e),
        )

