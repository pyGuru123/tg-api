from pydantic import BaseModel
from typing import Optional


class ImagineRequest(BaseModel):
    prompt: str
    style: str
    upscale: Optional[bool] = False

class ImageResponse(BaseModel):
	image: bytes

class coderunnerRequest(BaseModel):
	code: str
	lang: Optional[str] = "python"

class renderRequest(BaseModel):
	code: str
	theme: Optional[str] = "dark-plus"

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
