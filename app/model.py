from pydantic import BaseModel


class ImagineRequest(BaseModel):
    prompt: str
    style: str
    upscale: bool = False

class ImagineResponse(BaseModel):
	image: bytes