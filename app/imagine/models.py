# List all allowed models

MODELS = {
    "Absolute Reality V1.8.1": "absolutereality_v181.safetensors [3d9d4d2b]",
    "Anything V5": "anythingV5_PrtRE.safetensors [893e49b9]",
    "AbyssOrangeMix V3": "AOM3A3_orangemixs.safetensors [9600da17]",
    "Deliberate V2": "deliberate_v2.safetensors [10ec4b29]",
    "Dreamlike Diffusion V2": "dreamlike-diffusion-2.0.safetensors [fdcf65e7]",
    "Dreamshaper 8": "dreamshaper_8.safetensors [9d40847d]",
    "Eimis Anime Diffusion V1.0": "EimisAnimeDiffusion_V1.ckpt [4f828a15]",
    "Elldreth's Vivid": "elldreths-vivid-mix.safetensors [342d9d26]",
    "MeinaMix Meina V11": "meinamix_meinaV11.safetensors [b56ce717]",
    "Openjourney V4": "openjourney_V4.ckpt [ca2f377f]",
    "Portrait+ V1": "portraitplus_V1.0.safetensors [1400e684]",
    "Realistic Vision V5.0": "Realistic_Vision_V5.0.safetensors [614d1063]",
    "Redshift Diffusion V1.0": "redshift_diffusion-V10.safetensors [1400e684]",
    "ReV Animated V1.2.2": "revAnimated_v122.safetensors [3f4fefd9]",
    "SD V1.5": "v1-5-pruned-emaonly.ckpt [81761151]",
    "Shonin's Beautiful People V1.0": "shoninsBeautiful_v10.safetensors [25d8c546]",
    "Timeless V1": "timeless-1.0.ckpt [7c4971d4]"
}

def get_model(model_name):
    model = MODELS[model_name].replace(" ", "+")
    model = model.replace("[", "%5B").replace("]", "%5D")
    return model

def get_model_tensor(model):
    if not model:
        return get_model("Dreamshaper 8")

    return get_model(model)

async def all_models():
    return list(MODELS.keys())