import requests
import urllib.parse
from loguru import logger

def url_encode(input_string):
    encoded_string = urllib.parse.quote(input_string, safe='')
    return encoded_string

async def get_trackers():
	trackers = [
		"udp://glotorrents.pw:6969/announce",
		"udp://tracker.opentrackr.org:1337/announce",
		"udp://torrent.gresille.org:80/announce",
		"udp://tracker.openbittorrent.com:80",
		"udp://tracker.coppersurfer.tk:6969",
		"udp://tracker.leechers-paradise.org:6969",
		"udp://p4p.arenabg.ch:1337",
		"udp://tracker.internetwarriors.net:1337",
	]

	url_encoded_trackers = "&tr=".join(map(lambda tracker: url_encode(tracker), trackers))
	return url_encoded_trackers

async def create_magnet(name, hash):
	name = name.replace(" ", "%20")
	magnet = f"magnet:?xt=urn:btih:{hash}&dn={name}&tr={await get_trackers()}"
	return magnet

async def get_yts_magnet(movie):
	movie_name = movie.replace(" ", "%20")
	url = f"https://yts.mx/api/v2/list_movies.json?query_term={movie_name}"
	response = requests.get(url)
	all_data = response.json()
	result_set = []

	if all_data['status'] == 'ok':
		for data in all_data['data']['movies']:
			for torrent in data["torrents"][:3]:
				result = {
					"name": f"{data['title_long']} {torrent['quality']}",
					"size": torrent["size"],
					"seeders": str(torrent["seeds"]),
					"leechers": str(torrent["peers"]),
					"magnet": await create_magnet(data["title"], torrent['hash'])
				}
				result_set.append(result)

		return result_set

	return []
