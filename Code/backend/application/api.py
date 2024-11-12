from flask import current_app as app, jsonify
from flask_security import auth_required, SQLAlchemyUserDatastore, verify_password, hash_password, current_user
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from application.database import db
from application.models import Customer, User, ServiceProfessional


ds : SQLAlchemyUserDatastore = app.security.datastore

# Login Parser
login_parser = reqparse.RequestParser()
login_parser.add_argument("email")
login_parser.add_argument("password")

roles = {
    "rid": fields.Integer,
    "name": fields.String,
    "description": fields.String
}

authenticated_user = {
    "uid": fields.Integer,
    "email": fields.String,
    "roles": fields.List(fields.Nested(roles)),
    "token": fields.String
    }

customer = {
    "c_id": fields.Integer,
    "date_created": fields.DateTime,
    "f_name": fields.String,
    "l_name": fields.String,
    "description": fields.String
    }

admin = {
    "uid": fields.Integer,
    "email": fields.String, 
}

sp = {
    "sp_id": fields.Integer,
    "date_created": fields.DateTime,
    "f_name": fields.String,
    "l_name": fields.String,
    "description": fields.String,
    "service_type": fields.String,
    "experience": fields.Integer

}


class Welcome(Resource):
    def get(self):
        return {"message": "Welcome to Pro Services API 1.0.0"}, 200

class Login(Resource):
    @marshal_with(authenticated_user)
    def post(self):
        cred = login_parser.parse_args()
        email = cred.get("email", None)
        password = cred.get("password", None)

        if email is None:
            abort(400, message = "Email is missing")
        
        if password is None:
            abort(400, message = "Password is missing")
        
        user = ds.find_user(email = email)

        if (not user):
            abort(404, message = "Invalid Credentials")
        
        if(verify_password(password, user.password)):
            user.token = user.get_auth_token()
            return user, 200
        else:
            abort(404, message = "Invalid Credentials")
            
    
class Register(Resource):

    def post(self):
        pass

    
class CustomerResource(Resource):
    @auth_required('token')
    @marshal_with(customer)
    def get(self):
        current_customer = db.session.query(Customer).filter(Customer.c_id == current_user.uid).first()
        if not current_customer:
            abort(404, message = "Customer not found")
        return current_customer, 200
    

class AdminResource(Resource):
    @auth_required('token')
    @marshal_with(admin)
    def get(self):
        admin = current_user
        if not admin:
            abort(404, message = "Admin not found")
        return admin, 200
    

class SPResource(Resource):
    @auth_required('token')
    @marshal_with(sp)
    def get(self):
        current_sp = db.session.query(ServiceProfessional).filter(ServiceProfessional.sp_id == current_user.uid).first()
        if not current_sp:
            abort(404, message = "Service Professional not found")
        return current_sp, 200


    