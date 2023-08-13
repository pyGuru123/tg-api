import os
import platform
import requests
import random
import string
from loguru import logger

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

token = os.environ.get("HOTPOT_KEY")

ARTMAKER_MODELS = {
	"portrait": [50, "Photo Portrait 1"],
	"charcoal": [54, "Charcoal 1"],
	"animation": [61, "Animation 2"],
	"scifi": [64, "Sci-fi 1"],
	"retro": [80, "Retro Art"],
	"popart": [81, "Pop Art"],
	"concept": [126, "Concept Art 6"],
	"concept2": [142, "Portrait Concept Art 2"],
	"illustration": [130, "Illustration Art 3"],
	"hotpot": [140, "Hotpot Art 9"],
	"modern": [146, "Concept Art 7"],
	"game": [143, "Portrait Game 7"],
	"watercolor": [155, "Watercolor 2"],
	"pattern": [159, "Pattern 1"]
}

def get_art_maker_model(model):
    if not model:
        return get_model("concept2")

    return ARTMAKER_MODELS.get(model, [142, "Portrait Concept Art 2"])

async def artmaker_all_models():
    return list(ARTMAKER_MODELS.keys())

async def art_maker(prompt: str, model: ""):
	endpoint = "https://api.hotpot.ai/art-maker-sdte-zmjbcrr"
	alphabet = random.choice(string.ascii_uppercase)
	id_ = f"8-oQRQxZ{alphabet}IEx799A{alphabet}"

	style_id, style_label = get_art_maker_model(model)

	payload = {
	    "seedValue": -1,
	    "inputText": "cute looking girl portrait",
	    "width": 512,
	    "height": 512,
	    "styleId": style_id,
	    "styleLabel": style_label,
	    "isPrivate": True,
	    "requestId": id_,
	    "resultUrl": f"https://hotpotmedia.s3.us-east-2.amazonaws.com/{id_}.png"
    }

	headers = {
	  'Authorization': token
	}

	response = requests.request("POST", endpoint, headers=headers, data=payload)
	image_url = response.text.strip('"')
	logger.info(image_url)
	img_response = requests.get(image_url)
	return img_response.content
