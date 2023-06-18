from imaginepy import Imagine, Style, Ratio


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
		return style[style]
	except Exception:
		return Style.V4_CREATIVE


async def all_styles():
	return list(styles.keys())


async def imagineImg(prompt: str, style):
    imagine = Imagine()

    img_data = imagine.sdprem(
        prompt=prompt,
        style=get_style(style),
        ratio=Ratio.RATIO_16X9
    )

    if img_data is None:
        print("An error occurred while generating the image.")
        return

    img_data = imagine.upscale(image=img_data)
    return img_data