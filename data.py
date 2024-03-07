#data.py

import requests
import json
import config

def get_latest_headlines():
    print("Fetching news headlines...")
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={config.NEWS_API_KEY}'
    response = requests.get(url)
    #print("Response status code: ", response.status_code)
    #print("Response text: ", response.text)
    data = json.loads(response.text)
    return data['articles']

