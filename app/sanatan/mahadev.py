import random
import requests

GROUP = ['edited', 'mahadev', 'shivlinga']
MAX_INT = 150

def get_mahadev_pic():
	group = random.choice(GROUP)
	index = random.randint(1, MAX_INT)
	return f"https://raw.githubusercontent.com/pyGuru123/The-Mahadev-Api/main/assets/imgs/{group}{index}.jpg"