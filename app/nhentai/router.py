from fastapi import APIRouter
from typing import Union

from app.model import nhentaiRequest, nhentaiResponse
from app.nhentai.main import main

router = APIRouter()

@router.post("/fetch")
async def getNhentai(request: nhentaiRequest) -> Union[nhentaiResponse, dict]:
	try:
		id = request.id
		data = await main(id)
		return data
	except Exception as e:
		return {"messgae": "error", "error": str(e)}