import json
import requests

chatEndpoint = "https://api.pawan.krd/v1/chat/completions"
ipEndpoint = "https://api.pawan.krd/resetip"

resetIP = {
	"reset": False
}

async def search_gpt(apikey, prompt):
	headers = {
		'Authorization' : 'Bearer ' + apikey,
		'Content-Type': 'application/json'
	}

	data = {
		"model": "gpt-3.5-turbo",
		"max_tokens": 1500,
		"messages": [
          {"role": "user", "content": prompt},
        ]
	}

	if not resetIP['reset']:
		requests.post(ipEndpoint, headers=headers)

	response = requests.post(chatEndpoint, headers=headers, json=data)
	if response.status_code == 200:
		data = response.json()
		return data["choices"][0]["message"]["content"]
	else:
		return f"Request error: {response.status_code}, {response.text}"
