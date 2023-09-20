import os
import time
import platform
import requests
from loguru import logger
from requests_toolbelt.multipart.encoder import MultipartEncoder

if platform.system() == "Windows":
    from dotenv import load_dotenv

    load_dotenv()

TOKEN= os.environ.get("VYRO_TOKEN")

IMAGINE_MODELS = {
    "creative_v4": 31,
    "imagine_v4": 30,
    "imagine_v3": 28,
    "imagine_v1": 27,
    "portrait": 26,
    "realistic": 29,
    "anime": 21
}

def get_imagine_model(model):
    if not model:
        return IMAGINE_MODELS["imagine_v4"]

    return IMAGINE_MODELS.get(model, 30)

async def imagine_all_models():
    return list(IMAGINE_MODELS.keys())


async def imagine_art(prompt: str, model: str="imagine_v4"):
    style_id = get_imagine_model(model)
    url = "https://api.vyro.ai/v1/imagine/web/generations"

    payload = {
        'model_version': '1',
        'steps': '30',
        'seed': '988553',
        'cfg': '7.5',
        'aspect_ratio': '1:1',
        'prompt': prompt,
        'negative_prompt': 'ugly, deformedd, disfigured, low-quality, distorted, revolting, abhorrent, horrid, unseemly, \
                    unsightly, off-putting, unsatisfactory, second-rate, mediocre, lousy, poor-quality',
        'style_id': str(style_id)
    }

    multipart_data = MultipartEncoder(fields=payload)

    headers = {
      'Authorization': f"Bearer {TOKEN}",
      'Content-Type': multipart_data.content_type,
      'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"
    }

    response = requests.request("POST", url, headers=headers, data=multipart_data)
    return response.content