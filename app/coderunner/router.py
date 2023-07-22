from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from typing import Union

from app.coderunner.main import execute_code
from app.coderunner.main import plot_graph
from app.coderunner.main import pastebin
from app.coderunner.main import render_code, get_themes
from app.model import (
    coderunnerRequest,
    renderRequest,
    coderunnerResponse,
    ImageResponse,
    pastebinRequest,
)

router = APIRouter()


@router.post("/execute")
async def execute(request: coderunnerRequest) -> coderunnerResponse:
    """Takes in piece of any valid python code and returns it output"""
    try:
        code = request.code
        output = await execute_code(code)

        return coderunnerResponse(
            message="success",
            code=code,
            output=output,
            error="",
        )

    except Exception as e:
        return coderunnerResponse(message="error", code=code, output="", error=str(e))


@router.post("/plot")
async def plot(request: coderunnerRequest) -> Union[ImageResponse, coderunnerResponse]:
    """Takes in code to plot graph using matplotlib and numpy\n
       Example:\n

       x = [1, 2, 3]\n
       y = [1, 4, 9]\n
       plt.plot(x, y)\n
    """

    try:
        code = request.code
        data = await plot_graph(code)

        return Response(content=data, media_type="image/png")
    except Exception as e:
        return coderunnerResponse(message="error", code=code, output="", error=str(e))


@router.post("/paste")
async def paste(request: pastebinRequest) -> coderunnerResponse:
    try:
        code = request.code
        title = request.title
        output = await pastebin(code, title)
        return coderunnerResponse(
            message="success",
            code=code,
            output=output,
            error="",
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/render")
async def render(request: renderRequest) -> ImageResponse:
    try:
        code = request.code
        theme = request.theme
        data = await render_code(code, theme)
        return Response(content=data, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/themes")
async def themes() -> list[str]:
    try:
        return get_themes()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
