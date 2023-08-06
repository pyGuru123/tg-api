from pydantic import BaseModel
from typing import Optional


class ImagineRequest(BaseModel):
    prompt: str
    # style: str
    upscale: Optional[bool] = False


class ImageResponse(BaseModel):
    image: bytes


class coderunnerRequest(BaseModel):
    code: str
    lang: Optional[str] = "python"


class renderRequest(BaseModel):
    code: str
    theme: Optional[str] = "dark-plus"


class pastebinRequest(BaseModel):
    code: str
    title: str


class coderunnerResponse(BaseModel):
    message: str
    code: str
    output: str
    error: str


class sanatanResponse(BaseModel):
    message: str
    error: str
    date: str
    sunrise: str
    sunset: str
    shloka: str
    importance: str


class simpleRequest(BaseModel):
    query: str

class simpleResponse(BaseModel):
    message: str
    query: str
    content: str
    error: str

class llmRequest(BaseModel):
    prompt: str

class llmResponse(BaseModel):
    message: str
    prompt: str
    content: str
    error: str

class ImageUrlResponse(BaseModel):
    url: str

class gitaRequest(BaseModel):
    chapter: int
    verse: int

class gitaResponse(BaseModel):
    meaning: str
    text: str
    verse_number: str
    word_meanings: str
    transliteration: str
    hindi_meaning: str
    hindi_word_meanings: str