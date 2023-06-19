from imaginepy import Imagine, Ratio
from loguru import logger
from app.imagine.styles import STYLES


def get_style(style):
    try:
        return STYLES[style]
    except Exception:
        return STYLES["portrait"]


async def all_styles() -> list[str]:
    return list(STYLES.keys())


async def imagine(prompt: str, style: str) -> bytes:
    imagine = Imagine()
    style = get_style(style)

    logger.info(f"{prompt=}")
    logger.info(f"{style=}")
    
    img_data = imagine.sdprem(
        prompt=prompt,
        style=style,
        ratio=Ratio.RATIO_16X9
    )

    if img_data is None:
        logger.error("An error occurred while generating the image.")
        raise Exception("An error occurred while generating the image")

    if "--upscale" in prompt:
        img_data = imagine.upscale(image=img_data)

    return img_data