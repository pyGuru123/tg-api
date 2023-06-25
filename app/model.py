from pydantic import BaseModel
from typing import Optional, List


class ImagineRequest(BaseModel):
    prompt: str
    style: str
    upscale: bool = False

class ImageResponse(BaseModel):
	image: bytes

class nhentaiRequest(BaseModel):
	id: int

class nhentaiResponse(BaseModel):
	cdn_id: int
	num_pages: int
	cdn_url: str
	urls: List[str]

class coderunnerRequest(BaseModel):
	code: str
	lang: str = "python"

class coderunnerResponse(BaseModel):
	message: str
	code: str
	output: str
	error: str
