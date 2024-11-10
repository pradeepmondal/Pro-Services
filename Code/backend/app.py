from flask import Flask
import os
from application.config import DevConfig, Config
from application.database import db
from application.models import User, Role
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
from flask_restful import Api, Resource
from flask_cors import CORS


app = None

def create_app():
    app = Flask(__name__)

    if(os.getenv("ENV") == "dev"):
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(Config)

    datastore = SQLAlchemyUserDatastore(db, User, Role)

    db.init_app(app)
    app.security = Security(app, datastore=datastore, register_blueprint=False)
    CORS(app)
    api = Api(app)
    app.app_context().push()
    return app, api
    
app, api = create_app()

import application.init_data
from application.api import Welcome, Login, CustomerResource

api.add_resource(Welcome, '/')
api.add_resource(Login, '/login')
api.add_resource(CustomerResource, '/customer')

if __name__ == '__main__':
    app.run(port=5050)


