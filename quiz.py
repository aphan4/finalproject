import json
import urllib.parse
import urllib.request
import urllib.error

from data import FOODS

# google places API key lives in keys.py (git-ignored)
try:
    import keys
    API_KEY = keys.API_KEY
except (ImportError, AttributeError):
    API_KEY = ""


def recommend(answers):
    scored = []
    for food in FOODS:
        score = 0
        for key, value in answers.items():
            if value != "any" and food.get(key) == value:
                score += 1
        scored.append((score, food))
    # highest score first; ties keep their original order (stable sort)
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [food for score, food in scored[:3]]


def get_restaurants(search_term, location, limit=3):
    if not API_KEY:
        return []
    query = "{} restaurants in {}".format(search_term, location)
    params = {"query": query, "key": API_KEY}
    url = ("https://maps.googleapis.com/maps/api/place/textsearch/json?"
           + urllib.parse.urlencode(params))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, ValueError):
        return []
    if data.get("status") != "OK":
        return []

    results = []
    for place in data.get("results", [])[:limit]:
        place_id = place.get("place_id", "")
        results.append({
            "name": place.get("name", "Unknown"),
            "rating": place.get("rating"),
            "address": place.get("formatted_address", ""),
            "maps_url": "https://www.google.com/maps/place/?q=place_id:" + place_id,
        })
    return results


def has_key():
    return bool(API_KEY)