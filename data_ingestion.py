import uuid
from flask import jsonify
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
