from app.imagine.sync_imagine import Imagine
from app.imagine.constants import Ratio
from app.imagine.styles import STYLES

imagine_engine = Imagine()

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
        negative="ugly, deformed, disfigured, low-quality, distorted, revolting, abhorrent, horrid, unseemly, unsightly, off-putting, unsatisfactory, second-rate, mediocre, lousy, poor-quality"
    )

    if img_data is None:
        raise Exception("An error occurred while generating the image")

    if upscale:
        img_data = imagine.upscale(image=img_data)

    return img_data