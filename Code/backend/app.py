from flask import Flask
import os
from application.config import DevConfig, Config
from application.database import db
from application.models import User, Role
from flask_security import Security, SQLAlchemyUserDatastore, auth_required


app = None

def create_app():
    app = Flask(__name__)

    if(os.getenv("ENV") == "dev"):
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(Config)

    datastore = SQLAlchemyUserDatastore(db, User, Role)

    db.init_app(app)
    app.security = Security(app, datastore=datastore)
    app.app_context().push()
    return app
    
app = create_app()

import application.init_data

@app.get('/')
def welcome():
    return {"message": "Welcome to Pro Services"}


@app.get('/protected')
@auth_required()
def protected():
    return {"message": "Welcome to Protected Pro Services"}

if __name__ == '__main__':
    app.run(port=5050)


