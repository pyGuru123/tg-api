from fastapi import APIRouter
from typing import Union
from loguru import logger

from app.model import nhentaiRequest, nhentaiResponse
from app.nhentai.main import main

router = APIRouter()

@router.post("/get")
async def getNhentai(request: nhentaiRequest) -> Union[nhentaiResponse, dict]:
	id = request.id
	data = await main(id)
	return data