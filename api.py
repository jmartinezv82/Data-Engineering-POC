from dotenv import dotenv_values
from flask import Flask, jsonify
from flask_swagger import swagger
from pytz import utc
from flask_apscheduler import APScheduler
from data_ingestion import get_and_save_articles, get_articles_from_mongo

config = dotenv_values(".env")


# set configuration values
class Config:
    SCHEDULER_TIMEZONE = utc
    SCHEDULER_API_ENABLED = True


# create app
app = Flask(__name__)
app.config.from_object(Config())


@app.route("/")
def home():
    swag = swagger(app, from_file_keyword='swagger_from_file')
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Data Enfinerring POC"
    return jsonify(swag)


@app.route("/api/data/get", methods=['GET'])
def api_data_get():
    """
    An endpoint that return all articles saved in mongodb atlas service
    ---
    tags:
    - articles
    responses:
      200:
        description: Hacked some hacks
    """
    try:
        return jsonify(get_articles_from_mongo())
    except IndexError:
        return jsonify(IndexError)


# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


# interval examples
@scheduler.task("interval", id="do_save_info", minutes=30, misfire_grace_time=900)
def save_info():
    get_and_save_articles()


if __name__ == "__main__":
    app.run(debug=False)

