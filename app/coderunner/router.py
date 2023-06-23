from fastapi import APIRouter

from app.coderunner.main import execute_code
from app.model import coderunnerRequest, coderunnerResponse

router = APIRouter()

@router.post("/execute")
async def executor(request: coderunnerRequest) -> coderunnerResponse:
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
