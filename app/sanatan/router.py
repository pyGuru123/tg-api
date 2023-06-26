from fastapi import APIRouter
from typing import Union

from app.model import sanatanResponse
from app.sanatan.main import gitapress_data, todays_date

router = APIRouter()

@router.get("/today")
async def today() -> sanatanResponse:
	try:
		todays_data = await gitapress_data()
		response = sanatanResponse(**todays_data)

		return response

	except Exception as e:
		return sanatanResponse(
				message= "error",
				error= str(e),
				date= todays_date(),
				sunrise= "",
				sunset= "",
				shloka= "",
				importance= ""
			)