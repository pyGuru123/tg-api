from fastapi import APIRouter
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.model import llmRequest, llmResponse
from app.llmodels.llm import (
    ask_gpt4,
    ask_llama,
    ask_gemini
)

router = APIRouter()

@router.post("/gpt")
async def gpt4(request: llmRequest) -> llmResponse:
    """Search ChatGPT using gpt-4 model"""
    try:
        prompt = request.prompt
        context = request.context
        data = await ask_gpt4(prompt, context)
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

@router.post("/llama")
async def llama(request: llmRequest) -> llmResponse:
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


@router.post("/gemini")
async def gemini(request: llmRequest) -> llmResponse:
    """Search Google advanced AI Gemini"""
    try:
        prompt = request.prompt
        data = await ask_gemini(prompt)

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