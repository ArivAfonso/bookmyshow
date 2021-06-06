import requests
import re

def bookmyshow(city_name):
	""" Get Latest & Upcoming Movies Type & Name Data from BookMyShow.com """
	try:
		NOW_SHOWING_REGEX = """{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"Filter Impression:category\\\/now showing"},"products":\[{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}\]}}}"""
		COMING_SOON_REGEX = """{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"category\\\/coming soon"},"products":{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}}}}"""
		if city_name is not None:
			response = requests.get(f"https://in.bookmyshow.com/{city_name.lower()}/movies", headers={'User-Agent' : "Magic Browser"})
			showing_movies = [{
				"movie_name": data[0], "movie_id": data[1], "movie_type": data[3], "movie_language": data[5]
			} for data in re.findall(NOW_SHOWING_REGEX, response.text)]
			upcoming_movies = [{
				"movie_name": data[0], "movie_id": data[1], "movie_type": data[3], "movie_language": data[5]
			} for data in re.findall(COMING_SOON_REGEX, response.text)]
			return {"showing_movies": showing_movies, "upcoming_movies": upcoming_movies}
		else:
			return "Please Enter Valid City Name to Get Latest / Upcoming Movies List!"
	except Exception as ex:
		return f"Error: {ex}"