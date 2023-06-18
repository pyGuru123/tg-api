from imaginepy import Imagine, Style, Ratio
from loguru import logger


styles = {
    "anime": Style.ANIME_V2,
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
}

def get_style(style):
    try:
        return styles[style]
    except Exception:
        return Style.V4_CREATIVE


async def all_styles() -> list[str]:
    return list(styles.keys())


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