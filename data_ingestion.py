import uuid
import os
from dotenv import dotenv_values
from pymongo import MongoClient
import requests

config = dotenv_values(".env")
mongo_url_env = os.environ['MONGO_URL'] if config.get('MONGO_URL') is None else config.get('MONGO_URL')
api_env = os.environ['API'] if config.get('API') is None else config.get('API')

client = MongoClient(mongo_url_env)


def get_articles():
    r = requests.get(api_env + '/articles')
    return r.json()


def get_and_save_articles():
    articles_api = get_articles()
    db = client.news
    articles = db.articles
    docs = []

    for a in articles_api:
        to_save = a
        to_save['_id'] = str(uuid.uuid4())
        docs.append(to_save)

    result = articles.insert_many(docs)

    return {
        "status": 200,
        "documents_saved": len(result.inserted_ids)
    }


def get_articles_from_mongo():
    db = client.news
    articles = db.articles

    result = articles.find()

    return {
        "status": 200,
        "data": list(result)
    }
