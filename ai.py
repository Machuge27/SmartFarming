import requests


url = "https://google-web-search1.p.rapidapi.com/"

querystring = {"query": "World Cup", "limit": "20", "related_keywords": "true"}

headers = {
    "X-RapidAPI-Key": "62b6a70471msh25e8f2b9282e823p1acfc8jsn7f5fe6971ad1",
    "X-RapidAPI-Host": "google-web-search1.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
