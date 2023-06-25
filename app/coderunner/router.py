from fastapi import APIRouter
from fastapi.responses import Response
from typing import Union

from app.coderunner.main import execute_code
from app.coderunner.main import plot_graph
from app.model import coderunnerRequest, coderunnerResponse, ImageResponse

router = APIRouter()

@router.post("/execute")
async def execute(request: coderunnerRequest) -> coderunnerResponse:
	try:
		code = request.code
		output = await execute_code(code)

		return coderunnerResponse(
			message= "success",
			code= code,
			output= output,
			error= "",
		)

	except Exception as e:
		return coderunnerResponse(
			message= "error",
			code= code,
			output= "",
			error= str(e)
		)


@router.post("/plot")
async def plot(request: coderunnerRequest) -> Union[ImageResponse, coderunnerResponse]:
	try:
		code = request.code
		data = await plot_graph(code)

		return Response(content=data, media_type="image/png")
	except Exception as e:
		return coderunnerResponse(
			message= "error",
			code= code,
			output= "",
			error= str(e)
		)

