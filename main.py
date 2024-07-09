from flaskapp.app import create_app
import json
import os

if __name__ == "__main__" :
    config = json.load(open('config.json'))
    application = create_app(config, os.path.dirname(__file__))

    application.run(host=config["SERVER"]["IP"], port=config["SERVER"]["PORT"], debug=config["LOGGER"]["FLASK_DEBUG"])
    pass