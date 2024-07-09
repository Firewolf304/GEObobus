import os
import json

class DBConfig:
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    def __init__(self, dbname : str, user : str, password : str, host : str, port : str, protocol : str = "postgresql", track_modify : bool = False):
        self.SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','{}://{}:{}@{}:{}/{}'.format(protocol, user, password, host, port, dbname))
        self.SQLALCHEMY_TRACK_MODIFICATIONS = track_modify

    def __init__(self, config : json, track_modify : bool = False):
        self.SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','{}://{}:{}@{}:{}/{}'.format(config["PROTOCOL"], config["USER"], config["PASSWORD"], config["HOST"], config["PORT"], config["DBNAME"]))
        self.SQLALCHEMY_TRACK_MODIFICATIONS = track_modify
