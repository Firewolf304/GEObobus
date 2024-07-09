import importlib
import os

import flask
import json
from flaskapp.SQL.dbconfig import DBConfig
from flaskapp.SQL.database import db
from sqlalchemy import text
from flaskapp.logging.CustomLogger import logger
import flaskapp.SQL.models
from flaskapp.logging.formatter import CustomFormatter, ColoredFormatter
import logging
from pathlib import Path

def create_app(config : json, current_path : str):
    # logging
    filelogger = logging.FileHandler(config["LOGGER"]["FILENAME"])
    filelogger.setLevel(logging.DEBUG)
    filelogger.mode = "w+"
    ch = logging.StreamHandler()
    ch.setFormatter(ColoredFormatter(config["LOGGER"]["FORMAT"]))
    logging.basicConfig(level=getattr(logging, config["LOGGER"]["LOGLEVEL"]), format=config["LOGGER"]["FORMAT"], handlers=[filelogger, ch ])
    logger.info ("Starting service")

    # app
    app = flask.Flask(__name__, static_folder=config["SERVER"]["STATIC_FOLDER"], static_url_path=config["SERVER"]["STATIC_URL_PATH"])

    # routes
    module_path = Path(os.path.abspath(os.curdir), config["SERVER"]["ROUTES"])
    for folder in os.listdir(module_path):
        path = module_path / folder
        if(os.path.isdir(path)):
            path /= "main.py"
            logger.debug("Loading {}".format(folder))
            spec = importlib.util.spec_from_file_location("lib_{}".format(folder), path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, 'get_blueprint'):
                blueprint = module.get_blueprint()
                app.register_blueprint(blueprint)


    # db
    app.config.from_object(DBConfig(config["DATABASE"], track_modify=False))
    db.init_app (app)
    with app.app_context():
        logger.debug("Using sql engine: {}".format(db.engine.name))
        if(config["DATABASE"]["CREATE"]): db.create_all()
        if(config["DATABASE"]["REFLECT"]): db.reflect()
        try:
            db.session.execute(text('select * from users;'))
            logger.debug("SQL is alive")
        except Exception as e:
            logger.debug("SQL error: {}".format(e))
    return app
