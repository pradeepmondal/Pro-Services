import os

b_dir = os.path.dirname(__file__)
prod_db_d_path = os.path.join(b_dir, "../databases/prod")
dev_db_d_path = os.path.join(b_dir, "../databases/dev")


class Config():
    DEBUG = True
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + dev_db_d_path + "/devDB.sqlite3"
    SECRET_KEY = 'wifihsasecret'
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'hifihsasecret'
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'auth-token'
    SECURITY_TOKEN_MAX_AGE = 7200
    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 30
    CACHE_REDIS_PORT = 6379
    

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + dev_db_d_path + "/devDB.sqlite3"
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'hifihsasecret'
    SECRET_KEY = 'wifihsasecret'
    WTF_CSRF_ENABLED = False









