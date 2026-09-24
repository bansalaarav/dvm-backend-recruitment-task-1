import requests


API_KEY = "e5a42ecda37d8f4c72222b31cf1312e2"
BASE_URL = f"http://ws.audioscrobbler.com/2.0/"

headers = {"User-Agent": "aarav-lastfm-project/1.0"}

thing = {
    "artist": ["topartists", "artist"],
    "track": ["tracks", "track"]
}

def get_top_by_country(country, type_, limit):
    params = {
        "method": f"geo.gettop{type_}s",
        "country": country,
        "api_key": API_KEY,
        "format": "json",
        "limit": limit
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()[thing[type_][0]][thing[type_][1]]
    return data


def search(type_, query, limit):
    params = {
        "method": f"{type_}.search",
        "api_key": API_KEY,
        "format": "json",
        "limit": limit,
        f"{type_}": query
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()["results"][f"{type_}matches"][type_]
    return data


def get_charts(type_, limit):
    params = {
        "method": f"chart.gettop{type_}s",
        "api_key": API_KEY,
        "format": "json",
        "limit": limit,
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()[f"{type_}s"][type_]
    return data
