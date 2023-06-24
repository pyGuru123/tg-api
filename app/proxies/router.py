from fastapi import APIRouter

from app.model import proxyRequest, proxyResponse
from app.proxies.gpt import search_gpt

router = APIRouter()

@router.post("/gpt")
async def gpt(request: proxyRequest) -> proxyResponse:
	# try:
		apikey = request.apikey
		prompt = request.prompt
		response = await search_gpt(apikey, prompt)

		return proxyResponse(
			prompt= prompt,
			response= response
		)

	# except Exception as e:
	# 	return proxyResponse(
	# 		prompt= prompt,
	# 		response= str(e)
	# 	)