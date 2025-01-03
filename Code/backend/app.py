from flask import Flask, jsonify
import os
from application.config import DevConfig, Config
from application.database import db
from application.models import *
from flask_security import Security, SQLAlchemyUserDatastore
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_caching import Cache
from application.celery.celery_creator import celery_init_app
import flask_excel as excel

app = None

def create_app():
    app = Flask(__name__)

    if(os.getenv("ENV") == "dev"):
        app.config.from_object(Config)
    else:
        app.config.from_object(Config)

    datastore = SQLAlchemyUserDatastore(db, User, Role)

    db.init_app(app)
    celery_app = celery_init_app(app)
    cache = Cache(app)
    
    app.celery_app = celery_app
    app.cache = cache
    app.security = Security(app, datastore=datastore, register_blueprint=False)

    CORS(app)
    api = Api(app)
    app.app_context().push()
    return app, api
    
app, api = create_app()


celery_app = app.celery_app

import application.celery.celery_scheduler



import application.init_data
from application.api import Welcome, Login, CustomerResource, AdminResource, SPResource, CategoryList, ServiceList, CustomerList, ServiceResource, SPList, CategoryResource, SRResource, CustomerAddress, UnauthServiceList, SRListResource





api.add_resource(Welcome, '/')
api.add_resource(Login, '/login')
api.add_resource(CustomerResource, '/customer','/customer/<int:c_id>' , endpoint = 'customer')
api.add_resource(CustomerAddress, '/customer_address', endpoint = 'customer_address')
api.add_resource(AdminResource, '/admin', endpoint = 'admin')
api.add_resource(SPResource, '/sp', '/sp/<int:sp_id>', endpoint = 'sp')
api.add_resource(CategoryResource, '/service_category', '/service_category/<int:cat_id>', endpoint = 'service_category')
api.add_resource(CategoryList, '/service_categories', endpoint = 'service_categories')
api.add_resource(ServiceResource, '/service', '/service/<int:s_id>', endpoint='service')
api.add_resource(ServiceList, '/services','/services/<int:cat_id>', endpoint='service_list')
api.add_resource(CustomerList, '/customers', endpoint = 'customer_list')
api.add_resource(SPList, '/sps/<int:s_id>', endpoint = 'sp_list')
api.add_resource(SRResource, '/service_request/<int:sr_id>', '/service_request', endpoint = 'service_request')
api.add_resource(SRListResource, '/service_request/<int:c_id>/<int:sp_id>', endpoint = 'sr_list')
api.add_resource(UnauthServiceList, '/unauth_services', endpoint='unauth_service_list')

excel.init_excel(app)

if __name__ == '__main__':
    
    app.run(port=5050)


