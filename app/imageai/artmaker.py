import os
import platform
import requests
import random
import string
from loguru import logger

if platform.system() in ["Windows", "Linux"]:
    from dotenv import load_dotenv

    load_dotenv()

token = os.environ.get("HOTPOT_KEY")

ARTMAKER_MODELS = {
	"sketch_general_1": [1, "Sketch General 1"],
	"sketch_general_2": [2, "Sketch General 2"],
	"sketch_general_3": [3, "Sketch General 3"],
	"sketch_scribble_black_white_1": [4, "Sketch Scribble Black White 1"],
	"sketch_scribble_color_1": [5, "Sketch Scribble Color 1"],
	"icon_black_white": [6, "Icon Black White"],
	"icon_flat": [7, "Icon Flat"],
	"icon_sticker": [8, "Icon Sticker"],
	"sticker": [9, "Sticker"],
	"comic_book_1": [10, "Comic Book 1"],
	"comic_book_2": [11, "Comic Book 2"],
	"comic_book_3": [12, "Comic Book 3"],
	"doom_1": [13, "Doom 1"],
	"doom_2": [14, "Doom 2"],
	"watercolor_general_1": [15, "Watercolor General 1"],
	"japanese_art": [16, "Japanese Art"],
	"acrylic_art": [17, "Acrylic Art"],
	"graffiti": [18, "Graffiti"],
	"hotpot_art_1": [19, "Hotpot Art 1"],
	"hotpot_art_2": [20, "Hotpot Art 2"],
	"hotpot_art_3": [21, "Hotpot Art 3"],
	"hotpot_art_5": [22, "Hotpot Art 5"],
	"hotpot_art_6": [23, "Hotpot Art 6"],
	"pixel_art": [24, "Pixel Art"],
	"sculpture_general_1": [25, "Sculpture General 1"],
	"fantasy_1": [26, "Fantasy 1"],
	"fantasy_2": [27, "Fantasy 2"],
	"fantasy_3": [28, "Fantasy 3"],
	"anime_1": [29, "Anime 1"],
	"anime_black_white": [30, "Anime Black White"],
	"anime_berserk": [31, "Anime Berserk"],
	"anime_korean_1": [32, "Anime Korean 1"],
	"portrait_1": [33, "Portrait 1"],
	"portrait_2": [34, "Portrait 2"],
	"portrait_3": [35, "Portrait 3"],
	"portrait_mugshot": [36, "Portrait Mugshot"],
	"portrait_marble": [37, "Portrait Marble"],
	"portrait_gothic": [38, "Portrait Gothic"],
	"oil_painting_general_1": [39, "Oil Painting General 1"],
	"3d_black_white": [40, "3D Black White"],
	"3d_general_1": [41, "3D General 1"],
	"3d_print_1": [42, "3D Print 1"],
	"3d_general_2": [43, "3D General 2"],
	"3d_general_3": [44, "3D General 3"],
	"3d_voxel_1": [45, "3D Voxel 1"],
	"3d_minecraft_1": [46, "3D Minecraft 1"],
	"3d_roblox_1": [47, "3D Roblox 1"],
	"photo_volumetric_lighting_1": [48, "Photo Volumetric Lighting 1"],
	"photo_general_1": [49, "Photo General 1"],
	"photo_portrait_1": [50, "Photo Portrait 1"],
	"photo_product_1": [51, "Photo Product 1"],
	"photo_food_1": [52, "Photo Food 1"],
	"illustration_general_1": [53, "Illustration General 1"],
	"charcoal_1": [54, "Charcoal 1"],
	"charcoal_2": [55, "Charcoal 2"],
	"charcoal_3": [56, "Charcoal 3"],
	"steampunk": [57, "Steampunk"],
	"line_art": [58, "Line Art"],
	"gothic": [59, "Gothic"],
	"animation_1": [60, "Animation 1"],
	"animation_2": [61, "Animation 2"],
	"architecture_interior_modern_1": [62, "Architecture Interior Modern 1"],
	"architecture_general_1": [63, "Architecture General 1"],
	"sci-fi_1": [64, "Sci-fi 1"],
	"logo_detailed_1": [65, "Logo Detailed 1"],
	"logo_draft_1": [66, "Logo Draft 1"],
	"logo_clean_1": [67, "Logo Clean 1"],
	"logo_hipster_1": [68, "Logo Hipster 1"],
	"illustration_flat": [69, "Illustration Flat"],
	"animation_3": [70, "Animation 3"],
	"concept_art_2": [71, "Concept Art 2"],
	"cartoon_1": [72, "Cartoon 1"],
	"comic_book_4": [73, "Comic Book 4"],
	"architecture_interior_1": [74, "Architecture Interior 1"],
	"architecture_exterior_1": [75, "Architecture Exterior 1"],
	"comic_book_5": [76, "Comic Book 5"],
	"concept_art_3": [77, "Concept Art 3"],
	"stained_glass_1": [78, "Stained Glass 1"],
	"animation_4": [79, "Animation 4"],
	"retro_art": [80, "Retro Art"],
	"pop_art": [81, "Pop Art"],
	"illustration_smooth": [82, "Illustration Smooth"],
	"portrait_game_1": [83, "Portrait Game 1"],
	"concept_art_4": [84, "Concept Art 4"],
	"sci-fi_2": [85, "Sci-fi 2"],
	"sci-fi_3": [86, "Sci-fi 3"],
	"logo_sticker_1": [87, "Logo Sticker 1"],
	"painting_huang_gongwang_1": [88, "Painting Huang Gongwang 1"],
	"painting_claude_monet_1": [89, "Painting Claude Monet 1"],
	"painting_pablo_picasso_1": [90, "Painting Pablo Picasso 1"],
	"painting_paul_cezanne_1": [91, "Painting Paul Cezanne 1"],
	"painting_salvador_dali_1": [92, "Painting Salvador Dali 1"],
	"painting_vincent_van_gogh_1": [93, "Painting Vincent Van Gogh 1"],
	"3d_room_1": [94, "3D Room 1"],
	"portrait_figurine_1": [95, "Portrait Figurine 1"],
	"low_poly_1": [96, "Low Poly 1"],
	"low_poly_2": [97, "Low Poly 2"],
	"portrait_game_2": [98, "Portrait Game 2"],
	"portrait_game_3": [99, "Portrait Game 3"],
	"3d_portrait_1": [100, "3D Portrait 1"],
	"product_concept_art_1": [101, "Product Concept Art 1"],
	"line_art_2": [102, "Line Art 2"],
	"illustration_art_1": [103, "Illustration Art 1"],
	"illustration_art_2": [104, "Illustration Art 2"],
	"cute_art_1": [105, "Cute Art 1"],
	"anime_animal_1": [106, "Anime Animal 1"],
	"portrait_anime_1": [107, "Portrait Anime 1"],
	"portrait_anime_2": [108, "Portrait Anime 2"],
	"portrait_anime_3": [109, "Portrait Anime 3"],
	"portrait_anime_4": [110, "Portrait Anime 4"],
	"photo_portrait_2": [111, "Photo Portrait 2"],
	"photo_portrait_3": [112, "Photo Portrait 3"],
	"portrait_game_4": [113, "Portrait Game 4"],
	"fashion_1": [114, "Fashion 1"],
	"portrait_gothic_2": [115, "Portrait Gothic 2"],
	"logo_illustration_1": [116, "Logo Illustration 1"],
	"illustration_general_3": [117, "Illustration General 3"],
	"illustration_general_4": [118, "Illustration General 4"],
	"icon_minimal_1": [119, "Icon Minimal 1"],
	"icon_black_white_2": [120, "Icon Black White 2"],
	"icon_3d_1": [121, "Icon 3D 1"],
	"icon_cute_1": [122, "Icon Cute 1"],
	"illustration_general_2": [123, "Illustration General 2"],
	"isometric_1": [124, "Isometric 1"],
	"isometric_2": [125, "Isometric 2"],
	"concept_art_6": [126, "Concept Art 6"],
	"illustration_general_5": [127, "Illustration General 5"],
	"concept_art_5": [128, "Concept Art 5"],
	"portrait_game_5": [129, "Portrait Game 5"],
	"illustration_art_3": [130, "Illustration Art 3"],
	"portrait_6": [131, "Portrait 6"],
	"portrait_5": [132, "Portrait 5"],
	"portrait_game__6": [133, "Portrait Game  6"],
	"portrait_anime_5": [134, "Portrait Anime 5"],
	"portrait_4": [135, "Portrait 4"],
	"portrait_8": [136, "Portrait 8"],
	"portrait_9": [137, "Portrait 9"],
	"portrait_10": [138, "Portrait 10"],
	"hotpot_art_8": [139, "Hotpot Art 8"],
	"hotpot_art_9": [140, "Hotpot Art 9"],
	"portrait_concept_art_1": [141, "Portrait Concept Art 1"],
	"portrait_concept_art_2": [142, "Portrait Concept Art 2"],
	"portrait_game_7": [143, "Portrait Game 7"],
	"portrait_concept_art_3": [144, "Portrait Concept Art 3"],
	"hotpot_art_10": [145, "Hotpot Art 10"],
	"concept_art_7": [146, "Concept Art 7"],
	"oil_painting_2": [147, "Oil Painting 2"],
	"cyberpunk_1": [148, "Cyberpunk 1"],
	"cyberpunk_2": [149, "Cyberpunk 2"],
	"chinese_art_1": [150, "Chinese Art 1"],
	"chinese_art_2": [151, "Chinese Art 2"],
	"chinese_art_3": [152, "Chinese Art 3"],
	"japanese_art_2": [153, "Japanese Art 2"],
	"photo_moody_1": [154, "Photo Moody 1"],
	"watercolor_2": [155, "Watercolor 2"],
	"watercolor_3": [156, "Watercolor 3"],
	"watercolor_portrait_1": [157, "Watercolor Portrait 1"],
	"anime_cute_1": [158, "Anime Cute 1"],
	"fractal_pattern_1": [159, "Fractal Pattern 1"],
	"painting_fusion_1": [160, "Painting Fusion 1"],
	"photo_close_2": [161, "Photo Close 2"],
	"painting_fusion_3": [162, "Painting Fusion 3"],
	"sculpture_glass_1": [163, "Sculpture Glass 1"],
	"photo_dystopian_1": [164, "Photo Dystopian 1"],
	"painting_black_white_1": [165, "Painting Black White 1"],
	"painting_fusion_4": [166, "Painting Fusion 4"],
	"painting_fusion_5": [167, "Painting Fusion 5"],
	"painting_geometric_1": [168, "Painting Geometric 1"],
	"illustration_palette_1": [169, "Illustration Palette 1"],
	"watercolor_black_white_1": [170, "Watercolor Black White 1"],
	"photo_dystopian_2": [171, "Photo Dystopian 2"],
	"poster_war_zone_1": [172, "Poster War Zone 1"],
	"animation_5": [173, "Animation 5"],
	"portrait_anime_6": [174, "Portrait Anime 6"],
	"portrait_anime_7": [175, "Portrait Anime 7"],
	"photo_nyc_close_1": [176, "Photo NYC Close 1"],
	"photo_portrait_4": [177, "Photo Portrait 4"],
	"hotpot_art_11": [178, "Hotpot Art 11"],
	"hotpot_art_12": [179, "Hotpot Art 12"]
}

def get_art_maker_model(model):
    if not model:
        return ARTMAKER_MODELS.get("concept2", "")

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
	    "inputText": prompt,
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
	img_response = requests.get(image_url)
	return img_response.content
