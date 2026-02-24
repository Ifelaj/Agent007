import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_mobile_news(country="ng"):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=technology&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("articles", [])
