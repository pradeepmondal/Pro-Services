import os

b_dir = os.path.dirname(__file__)
prod_db_d_path = os.path.join(b_dir, "../databases/prod")
dev_db_d_path = os.path.join(b_dir, "../databases/dev")


class Config():
    DEBUG = False
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + prod_db_d_path + "/prodDB.sqlite3"
    

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + dev_db_d_path + "/devDB.sqlite3"
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'hifihsasecret'
    SECRET_KEY = 'wifihsasecret'
    WTF_CSRF_ENABLED = False









