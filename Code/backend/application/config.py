import os

b_dir = os.path.dirname(__file__)



class Config():
    DEBUG = False
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False





class DevConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + dev_db_d_path + "/devDB.sqlite3"






