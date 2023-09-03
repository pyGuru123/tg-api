import requests
from loguru import logger

async def create_magnet(name, hash):
	name = name.replace(" ", "%20")
	magnet = f"magnet:?xt=urn:btih:{hash}&dn={name}&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.bittor.pw%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Fbt.xxx-tracker.com%3A2710%2Fannounce&tr=udp%3A%2F%2Fpublic.popcorn-tracker.org%3A6969%2Fannounce&tr=udp%3A%2F%2Feddie4.nl%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce"
	return magnet

async def get_yts_magnet(movie):
	movie_name = movie.replace(" ", "%20")
	url = f"https://yts.mx/api/v2/list_movies.json?query_term={movie_name}"
	response = requests.get(url)
	all_data = response.json()
	result_set = []

	if all_data['status'] == 'ok':
		for data in all_data['data']['movies']:
			logger.info(data['torrents'])
			for torrent in data["torrents"][:3]:
				result = {
					"name": f"{data['title_long']} {torrent['quality']}",
					"size": torrent["size"],
					"magnet": await create_magnet(torrent['hash'], data["title_long"])
				}
				result_set.append(result)

		return result_set

	return []
