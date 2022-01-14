import datetime
import uuid

from dotenv import dotenv_values
from pymongo import MongoClient
import requests

config = dotenv_values(".env")
client = MongoClient(config.get('MONGO_URL'))


def get_articles():
    r = requests.get(config.get('API') + '/articles')
    return r.json()


def get_and_save_articles():
    articles_api = get_articles()
    db = client.news
    articles = db.articles

    result = articles.insert_many(articles_api)

    return {
        "status": 200,
        "documents_saved": len(result.inserted_ids)
    }

