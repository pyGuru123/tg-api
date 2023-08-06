from typing import Any, Optional, Tuple
from requests import Session, Response
from requests_toolbelt.multipart.encoder import MultipartEncoder
from langdetect import detect

from .constants import *

from app.imagine.constants import Ratio
from app.imagine.styles import STYLES
from app.imagine.constants import Style

STYLES = {
    "anime": Style.ANIME_V2,
    "portrait": Style.PORTRAIT,
    "creative": Style.V4_CREATIVE,
    "cosmic": Style.COMIC_V2,
    "marble": Style.MARBLE,
    "disney": Style.DISNEY,
    "minecraft": Style.MINECRAFT,
    "macro": Style.MACRO_PHOTOGRAPHY,
    "gta": Style.GTA,
    "ghibli": Style.STUDIO_GHIBLI,
    "dystopian": Style.DYSTOPIAN,
    "surreal": Style.SURREALISM,
    "graffiti": Style.GRAFFITI,
    "realistic": Style.REALISTIC,
    "comic": Style.COMIC_V2,
    "rainbow": Style.RAINBOW,
    "medieval": Style.MEDIEVAL,
    "origami": Style.ORIGAMI,
    "pattern": Style.PATTERN,
    "fantasy": Style.FANTASY,
    "neon": Style.NEON,
    "haunted": Style.HAUNTED,
    "kawaii": Style.KAWAII_CHIBI,
    "samurai": Style.SAMURAI,
    "painting": Style.PAINTING,
    "icon": Style.ICON,
    "cyberpunk": Style.CYBERPUNK,
    "architecture": Style.ARCHITECTURE,
    "retro": Style.RETRO,
    "futuristic": Style.FUTURISTIC,
    "polaroid": Style.POLAROID,
    "sketch": Style.SKETCH,
    "chromatic": Style.CHROMATIC,
    "popart": Style.POP_ART,
}


def validate_cfg(cfg: float) -> str:
    """Validates the cfg parameter."""
    if cfg < 0.0 or cfg > 16.0:
        raise ValueError(f"Invalid CFG, must be in range (0; 16), {cfg}")
    return str(cfg)


class Imagine:
    """Class for handling API requests to the Imagine service."""

    HEADERS = {"accept": "*/*", "user-agent": "okhttp/4.10.0"}

    def __init__(self, style: Style = Style.IMAGINE_V1):
        self.asset = "https://1966211409.rsc.cdn77.org"
        self.api = "https://inferenceengine.vyro.ai"
        if style is not None:
            self.HEADERS["style-id"] = str(style.value[0])  # accepts as string
        self.session = Session()
        self.version = "1"

    def _request(self, **kwargs) -> Response:
        """Sends a request to the server and returns the response."""
        headers = self.HEADERS
        headers.update(kwargs.get("headers", {}))

        response = self.session.request(
            method=kwargs.get("method", "GET").upper(),
            url=kwargs.get("url"),
            params=kwargs.get("params"),
            data=kwargs.get("data"),
            headers=headers,
        )

        response.raise_for_status()
        return response

    def _build_multipart_data(self, fields: dict) -> Tuple[MultipartEncoder, dict]:
        """Helper function to build multipart form data."""
        multi = MultipartEncoder(fields=fields)
        headers = {"content-type": multi.content_type}
        return multi, headers

    def assets(self, style: Style = Style.IMAGINE_V1) -> bytes:
        """Gets the assets."""
        return self._request(
            url=f"{self.asset}/appStuff/imagine-fncisndcubnsduigfuds//assets/{style.value[2]}/{style.value[1]}.webp"
        ).content

    def variate(
        self, image: bytes, prompt: str, style: Style = Style.IMAGINE_V1
    ) -> bytes:
        """Variates the character."""
        multi, headers = self._build_multipart_data(
            {
                "model_version": self.version,
                "prompt": prompt + (style.value[3] or ""),
                "strength": "0",
                "style_id": str(style.value[0]),
                "image": ("image.png", image, "image/png"),
            }
        )

        return self._request(
            method="POST", url=f"{self.api}/variate", data=multi, headers=headers
        ).content

    def sdprem(
        self,
        prompt: str,
        negative: str = None,
        priority: str = None,
        steps: str = None,
        high_res_results: str = None,
        style: Style = Style.IMAGINE_V1,
        seed: str = None,
        ratio: Ratio = Ratio.RATIO_1X1,
        cfg: float = 9.5,
    ) -> bytes:
        """Generates AI Art."""
        try:
            validated_cfg = validate_cfg(cfg)
        except Exception as e:
            raise ValueError(f"An error occurred while validating cfg: {e}")

        try:
            return self._request(
                method="POST",
                url=f"{self.api}/sdprem",
                data={
                    "model_version": self.version,
                    "prompt": prompt + (style.value[3] or ""),
                    "negative_prompt": negative or "",
                    "style_id": style.value[0],
                    "aspect_ratio": ratio.value,
                    "seed": seed or "",
                    "steps": steps or "30",
                    "cfg": validated_cfg,
                    "priority": priority or "0",
                    "high_res_results": high_res_results or "0",
                },
            ).content
        except Exception as e:
            raise ConnectionError(f"An error occurred while making the request: {e}")

    def upscale(self, image: bytes) -> bytes:
        """Upscales the image."""
        try:
            multi, headers = self._build_multipart_data(
                {
                    "model_version": self.version,
                    "image": ("test.png", image, "image/png"),
                }
            )
        except Exception as e:
            raise ConnectionError(
                f"An error occurred while building the multipart data: {e}"
            )

        try:
            return self._request(
                method="POST", url=f"{self.api}/upscale", data=multi, headers=headers
            ).content
        except Exception as e:
            raise ConnectionError(f"An error occurred while making the request: {e}")

    def translate(self, prompt: str) -> str:
        """Translates the prompt."""
        multi, headers = self._build_multipart_data(
            {"q": prompt, "source": detect(prompt), "target": "en"}
        )

        return self._request(
            method="POST", url=f"{self.api}/translate", data=multi, headers=headers
        ).json()["translatedText"]

    def interrogator(self, image: bytes) -> str:
        """Generates a prompt."""
        multi, headers = self._build_multipart_data(
            {
                "model_version": str(self.version),
                "image": ("prompt_generator_temp.png", image, "application/zip"),
            }
        )

        return self._request(
            method="POST", url=f"{self.api}/interrogator", data=multi, headers=headers
        ).text

    def sdimg(
        self,
        image: bytes,
        prompt: str,
        negative: str = None,
        seed: str = None,
        cfg: float = 9.5,
    ) -> bytes:
        """Performs inpainting."""
        multi, headers = self._build_multipart_data(
            {
                "model_version": self.version,
                "prompt": prompt,
                "negative_prompt": negative or "",
                "seed": seed or "",
                "cfg": validate_cfg(cfg),
                "image": ("image.png", image, "image/png"),
            }
        )

        return self._request(
            method="POST", url=f"{self.api}/sdimg", data=multi, headers=headers
        ).content

    def controlnet(
        self,
        image: bytes,
        prompt: str,
        negative: str = None,
        cfg: float = 9.5,
        control: Control = Control.SCRIBBLE,
        style: Style = Style.IMAGINE_V1,
        seed: str = None,
    ) -> bytes:
        """Performs image remix."""
        multi, headers = self._build_multipart_data(
            {
                "model_version": self.version,
                "prompt": prompt + (style.value[3] or ""),
                "negative_prompt": negative or "",
                "strength": "0",
                "cfg": validate_cfg(cfg),
                "control": control.value,
                "style_id": str(style.value[0]),
                "seed": seed or "",
                "image": ("image.png", image, "image/png"),
            }
        )

        return self._request(
            method="POST", url=f"{self.api}/controlnet", data=multi, headers=headers
        ).content


def get_style(style):
    try:
        return STYLES[style]
    except Exception:
        return STYLES["realistic"]


async def all_styles() -> list[str]:
    return list(STYLES.keys())


async def imagine(prompt: str, style: str, upscale: bool) -> bytes:
    style = get_style(style)

    img_data = imagine_engine.sdprem(
        prompt=prompt,
        style=style,
        ratio=Ratio.RATIO_16X9,
        negative="ugly, deformed, disfigured, low-quality, distorted, revolting, abhorrent, horrid, unseemly, unsightly, off-putting, unsatisfactory, second-rate, mediocre, lousy, poor-quality",
    )

    if img_data is None:
        raise Exception("An error occurred while generating the image")

    if upscale:
        img_data = imagine.upscale(image=img_data)

    return img_data