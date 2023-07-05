from fastapi import APIRouter
from typing import Union
from fastapi.responses import Response

from app.model import llmRequest, llmResponse
from app.llmodels.bard import ask_bard

router = APIRouter()


@router.post("/bard")
async def bard(request: llmRequest) -> dict:
    try:
        prompt = request.prompt
        data = await ask_bard(prompt)

        return {"message": "success", "prompt": prompt, "content": data, "error": ""}
    except Exception as e:
        return {"message": "error", "prompt": prompt, "content": "", "error": str(e)}
