from pydantic import BaseModel


class ImagineRequest(BaseModel):
    prompt: str
    style: str
    upscale: bool = False

class ImageResponse(BaseModel):
	image: bytes

class coderunnerRequest(BaseModel):
	code: str
	lang: str = "python"

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
