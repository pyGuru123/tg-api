import json
import requests

from app.config import ELEVENLABS_ENDPOINT

async def text_to_speech(text):
	payload = json.dumps({
	  "text": text,
	  "model_id": "eleven_multilingual_v2"
	})

	headers = {
	  'Content-Type': 'application/json'
	}

	response = requests.request("POST", ELEVENLABS_ENDPOINT, headers=headers, data=payload)
	return response.content