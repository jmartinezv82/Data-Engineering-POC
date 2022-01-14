from dotenv import dotenv_values
from pymongo import MongoClient
from flask import Flask, jsonify
from flask_swagger import swagger
from data_ingestion import get_and_save_articles

config = dotenv_values(".env")
client = MongoClient(config.get('MONGO_URL'))

app = Flask(__name__)


@app.route("/")
def home():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Data Enfinerring POC"
    return jsonify(swag)


@app.route("/api/data/get")
def api_data_get():
    try:
        return jsonify(get_and_save_articles())
    except IndexError:
        return jsonify(IndexError)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
