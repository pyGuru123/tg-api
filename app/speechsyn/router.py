from fastapi import APIRouter
from typing import Union
from fastapi.responses import Response
from loguru import logger

from app.model import ttsRequest
from app.speechsyn.tts import text_to_speech

router = APIRouter()


@router.post("/tts")
async def tts(request: ttsRequest):
    """Convert Text to speech with ElevenLabs Api"""
    try:
        text = request.text
        audio_bytes = await text_to_speech(text)

        headers = {
            "Content-Disposition": "attachment; filename=generated_audio.wav"
        }

        return Response(
            content=audio_bytes, media_type="audio/wav", headers=headers
        )
    except Exception as e:
        return {"message": "error", "text": text, "content": None, "error": str(e)}