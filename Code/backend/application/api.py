from flask import current_app as app, jsonify, request
from flask_security import auth_required, SQLAlchemyUserDatastore, verify_password, hash_password, current_user
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from application.database import db
from application.models import Customer, User, ServiceProfessional, Category, Service


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
    "email": fields.String,
    "active": fields.Boolean,
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

category = {
    "cat_id": fields.Integer,
    "name": fields.String,
    "description": fields.String
}

service = {
    "s_id": fields.String,
    "name": fields.String,
    "price": fields.Integer,
    "req_time": fields.Float,
    "description": fields.String,
    "cat_id": fields.Integer
}

def check_for_role():
    if request.endpoint in ['admin']:
        user_roles = [role.name for role in current_user.roles]
        if 'admin' not in user_roles:
            abort(403, message = "Incorrect role, forbidden")
    
    if request.endpoint in ['customer']:
        user_roles = [role.name for role in current_user.roles]
        if 'customer' not in user_roles:
            abort(403, message = "Incorrect role, forbidden")
    
    if request.endpoint in ['sp']:
        user_roles = [role.name for role in current_user.roles]
        if 'sp' not in user_roles:
            abort(403, message = "Incorrect role, forbidden")

def check_admin_role():
    user_roles = [role.name for role in current_user.roles]
    if 'admin' not in user_roles:
        abort(403, message = "Incorrect role, forbidden")


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
        current_customer.email = current_user.email
        current_customer.active = current_user.active
        return current_customer, 200
    

class AdminResource(Resource):
    @auth_required('token')
    @marshal_with(admin)
    def get(self):
        check_for_role()
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


class CategoryList(Resource):
    @auth_required('token')
    @marshal_with(category)
    def get(self):
        cat_list = db.session.query(Category).all()
        return cat_list, 200


class ServiceList(Resource):
    @auth_required('token')
    @marshal_with(service)
    def get(self, cat_id):
        services = db.session.query(Service).filter(Service.cat_id == cat_id).all()
        if(not services):
            abort(404, message = "No Services in this category")
        return services, 200
    
class CustomerList(Resource):
    @auth_required('token')
    @marshal_with(customer)
    def get(self):
        customers = db.session.query(Customer).all()
        if(not customers):
            abort(404, message = "No customers found")
        for customer in customers:
            customer.email = db.session.query(User).filter(User.uid == customer.c_id).first().email
            customer.active = db.session.query(User).filter(User.uid == customer.c_id).first().active
        return customers, 200