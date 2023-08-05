from fastapi import APIRouter
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.model import llmRequest, llmResponse
from app.llmodels.bard import ask_bard
from app.llmodels.chimera import ask_gpt, ask_llama

router = APIRouter()


@router.post("/gpt")
async def gpt(request: llmRequest) -> llmResponse:
    """Search ChatGPT using gpt-3.5-turbo model"""
    try:
        prompt = request.prompt
        data = await ask_gpt(prompt)
        logger.info(f"{data=}")

        return llmResponse(
            message="success",
            prompt=prompt,
            content=data,
            error=""
        )
    except Exception as e:
        return llmResponse(
            message="error",
            prompt=prompt,
            content="",
            error=str(e)
        )

@router.post("/bard")
async def bard(request: llmRequest) -> llmResponse:
    """Search Google Bard in a sessioned state"""
    try:
        prompt = request.prompt
        data = await ask_bard(prompt)

        return llmResponse(
            message="success",
            prompt=prompt,
            content=data,
            error=""
        )
    except Exception as e:
        return llmResponse(
            message="error",
            prompt=prompt,
            content="",
            error=str(e)
        )

@router.post("/llama")
async def gpt(request: llmRequest) -> llmResponse:
    """Search newly released Meta Lllama2""" 
    try:
        prompt = request.prompt
        data = await ask_llama(prompt)

        return llmResponse(
            message="success",
            prompt=prompt,
            content=data,
            error=""
        )
    except Exception as e:
        return llmResponse(
            message="error",
            prompt=prompt,
            content="",
            error=str(e)
        )
