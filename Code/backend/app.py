from flask import Flask
import os
from application.config import DevConfig, Config
from application.database import db


app = None

def create_app():
    app = Flask(__name__)

    if(os.getenv("ENV") == "dev"):
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(Config)

    db.init_app(app)
    app.app_context().push()
    return app
    
app = create_app()

if __name__ == '__main__':
    app.run(port=5050)


