from flask import current_app as app, jsonify, request
from flask_security import auth_required, SQLAlchemyUserDatastore, verify_password, hash_password, current_user
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from application.database import db
from application.models import Customer, User, ServiceProfessional, Category, Service, ServiceRequest
from werkzeug.utils import secure_filename
import os


ds : SQLAlchemyUserDatastore = app.security.datastore

CATEGORY_UPLOAD_FOLDER = 'static/service_category'
SERVICE_UPLOAD_FOLDER = 'static/service'
EXTENSIONS = {'png', 'jpg', 'gif', 'jpeg'}
app.config['CATEGORY_UPLOAD_FOLDER'] = CATEGORY_UPLOAD_FOLDER
app.config['SERVICE_UPLOAD_FOLDER'] = SERVICE_UPLOAD_FOLDER



# Login Parser
login_parser = reqparse.RequestParser()
login_parser.add_argument("email")
login_parser.add_argument("password")

# Category Parser
category_parser = reqparse.RequestParser()
category_parser.add_argument("name", type=str, required=True)
category_parser.add_argument("description", type=str, required=True)
# category_parser.add_argument("thumbnail", type='FileStorage', location='files')


# Service Parser
service_parser = reqparse.RequestParser()
service_parser.add_argument("s_id")
service_parser.add_argument("name")
service_parser.add_argument("base_price")
service_parser.add_argument("req_time")
service_parser.add_argument("description")
service_parser.add_argument("cat_id")
service_parser.add_argument("_method")

# Customer Parser
customer_parser = reqparse.RequestParser()
customer_parser.add_argument("f_name")
customer_parser.add_argument("l_name")
customer_parser.add_argument("email")
customer_parser.add_argument("password")


# Service Request Parser
sr_parser = reqparse.RequestParser()
sr_parser.add_argument("s_id")
sr_parser.add_argument("c_id")
sr_parser.add_argument("sp_id")
sr_parser.add_argument("description")
sr_parser.add_argument("status")


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
    "description": fields.String,
    "address": fields.String,
    "loc_pincode": fields.String
    }

admin = {
    "uid": fields.Integer,
    "email": fields.String, 
}

sp = {
    "sp_id": fields.Integer,
    "email": fields.String,
    "active": fields.Boolean,
    "date_created": fields.DateTime,
    "f_name": fields.String,
    "l_name": fields.String,
    "description": fields.String,
    "service_type": fields.String,
    "experience": fields.Integer,
    "price": fields.Integer,
    "rating": fields.Float

}

category = {
    "cat_id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "thumbnail_url": fields.String
}

service = {
    "s_id": fields.Integer,
    "name": fields.String,
    "base_price": fields.Integer,
    "req_time": fields.Float,
    "description": fields.String,
    "cat_id": fields.Integer
}

service_request = {
    "sr_id": fields.Integer,
    "s_id": fields.Integer,
    "c_id": fields.Integer,
    "sp_id": fields.Integer,
    "description": fields.String,
    "request_date": fields.DateTime,
    "completion_date": fields.DateTime,
    "status": fields.String,
    "remarks": fields.String
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
    
    def post(self):
        args = customer_parser.parse_args()
        f_name = args.get("f_name", None)
        l_name = args.get("l_name", None)
        email = args.get("email", None)
        password = args.get("password", None)
        if(not f_name):
            abort(400, message = "First Name is missing")
        if(not email):
            abort(400, message = "Price is missing")
        if(not password):
            abort(400, message = "Required Time is missing")

        customer = ds.find_user(email = email)

        if(customer):
            abort(400, message = "User with the email already exists")

        ds.create_user(email = email, password = hash_password(password), roles = ['customer'])
        customer_user = ds.find_user(email = email)
        customer_data = Customer(c_id = customer_user.uid, f_name = f_name, l_name = l_name, email = email )
        db.session.add(customer_data)
        db.session.commit()

        return "Registration Successful", 200



class CustomerAddress(Resource):
    @auth_required('token')
    def put(self):
        address = request.form.get('address')
        pincode = request.form.get('pincode')

        customer = db.session.query(Customer).filter(Customer.c_id == current_user.uid).first()

        if not customer:
            abort(404, "Customer Details not available")
        
        customer.address = address
        customer.loc_pincode = pincode

        db.session.add(customer)
        db.session.commit()

        return "Address successfully added"




    

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
    

class SPList(Resource):
    @auth_required('token')
    @marshal_with(sp)
    def get(self, s_id ):
        splist = db.session.query(ServiceProfessional).filter(ServiceProfessional.service_type == s_id).all()
        if(not splist):
            abort(404, message = "No Service Professional found for the given service")
        for sp in splist:
            sp.email = db.session.query(User).filter(User.uid == sp.sp_id).first().email
            sp.active = db.session.query(User).filter(User.uid == sp.sp_id).first().active
        return splist, 200
    
    @auth_required('token')
    @marshal_with(sp)
    def get(self):
            splist = db.session.query(ServiceProfessional).all()
            if(not splist):
                abort(404, message = "No Service Professional found")
            for sp in splist:
                sp.email = db.session.query(User).filter(User.uid == sp.sp_id).first().email
                sp.active = db.session.query(User).filter(User.uid == sp.sp_id).first().active
            return splist, 200
        
        



class CategoryResource(Resource):
    @auth_required('token')
    @marshal_with(category)
    def get(self, cat_id ):
        cat = db.session.query(Category).filter(Category.cat_id == cat_id).first()
        if not cat:
            abort(404, message = "Category not found")
        return cat, 200
    
    @auth_required('token')
    def post(self):
        
        name = request.form.get('name')
        description = request.form.get('description')
        thumbnail = request.files.get('thumbnail')
        thumbnail_path = None

        if(not name):
            abort(400, message = "Name is missing")
        if(not description):
            abort(400, message = "Description is missing")
        if(not thumbnail):
            abort(400, message = "Thumbnail is missing")

        if thumbnail.filename.split('.')[1].lower() in EXTENSIONS:
            path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(name + '.' + thumbnail.filename.split('.')[1].lower()))
            thumbnail.save(path)
            thumbnail_path = path

        category = Category(name = name, description = description, thumbnail_url = thumbnail_path)

        db.session.add(category)
        db.session.commit()

        return "Category successfully created", 200
    

    @auth_required('token')
    def delete(self, cat_id):
        category = db.session.query(Category).filter(Category.cat_id == cat_id).first()
        os.remove(category.thumbnail_url)
        db.session.delete(category)
        db.session.commit()

        return "Successfully Deleted", 200



        






class ServiceResource(Resource):
    @auth_required('token')
    def post(self):
        
        check_admin_role()
        name = request.form.get('name')
        base_price = request.form.get('base_price')
        req_time = request.form.get('req_time')
        description = request.form.get('description')
        cat_id = request.form.get('cat_id')

        thumbnail = request.files.get('thumbnail')



        
        if(not name):
            abort(400, message = "Name is missing")
        if(not base_price):
            abort(400, message = "Price is missing")
        if(not req_time):
            abort(400, message = "Required Time is missing")
        if(not description):
            abort(400, message = "Description is missing")
        if(not cat_id):
            abort(400, message = "Category is missing")

        if thumbnail.filename.split('.')[1].lower() in EXTENSIONS:
            path = os.path.join(app.config['SERVICE_UPLOAD_FOLDER'], secure_filename(name + '.' + thumbnail.filename.split('.')[1].lower()))
            thumbnail.save(path)
            thumbnail_path = path


        new_service = Service(name = name, base_price = base_price, req_time = req_time, description = description, cat_id = cat_id, thumbnail_url = thumbnail_path)

        db.session.add(new_service)
        db.session.commit()

        return "Service successfully added", 200
    

    @auth_required('token')
    def delete(self, s_id):
        check_admin_role()
        service = db.session.query(Service).filter(Service.s_id == s_id).first()
        if service.thumbnail_url:
            os.remove(service.thumbnail_url)
        db.session.delete(service)
        db.session.commit()

        return "Successfully Deleted", 200






    @auth_required('token')
    def put(self):
        check_admin_role()
        args = service_parser.parse_args()
        
        
        s_id = args.get("s_id", None)
        name = args.get("name", None)
        base_price = args.get("base_price", None)
        req_time = args.get("req_time", None)
        description = args.get("description", None)
        cat_id = args.get("cat_id", None)
        

        if(not s_id):
            abort(400, message = "Service Id is missing")
        if(not name):
            abort(400, message = "Name is missing")
        if(not base_price):
            abort(400, message = "Price is missing")
        if(not req_time):
            abort(400, message = "Required Time is missing")
        if(not description):
            abort(400, message = "Description is missing")
        if(not cat_id):
            abort(400, message = "Category is missing")
        
        service = db.session.query(Service).filter(Service.s_id == s_id).first()

        

        service.name = name
        service.base_price = base_price
        service.req_time = req_time
        service.description = description
        service.cat_id = cat_id

        # if(_method == 'POST'):
        #     service = Service(s_id = 'abcd', name = name, price = price, req_time = req_time, description = description, cat_id = cat_id)
        #     # handle s_id

        db.session.add(service)
        db.session.commit()

        return "Successfully updated", 200


class SRResource(Resource):
    @auth_required('token')
    @marshal_with(service_request)
    def get(self, sr_id):
        service_request = db.session.query(ServiceRequest).filter(ServiceRequest.sr_id == sr_id).first()
        if not service_request:
            abort(404, message = "SR not found")
        return service_request, 200
    
    def post(self):
        args = sr_parser.parse_args()
        s_id = args.get("s_id", None)
        c_id = args.get("c_id", None)
        sp_id = args.get("sp_id", None)
        description = args.get("description", None)
        status = args.get("status", None)
        
        if(not s_id):
            abort(400, message = "Service Id is missing")
        if(not c_id):
            abort(400, message = "Customer Id is missing")
        if(not sp_id):
            abort(400, message = "SP Id is missing")
        if(not description):
            abort(400, message = "Description Id is missing")
        if(not status):
            abort(400, message = "Status is missing")

    
        new_sr = ServiceRequest(s_id = s_id, c_id = c_id, sp_id = sp_id, description = description, status = status )
        db.session.add(new_sr)
        db.session.commit()

        return "Service Request Created", 200




class CategoryList(Resource):
    @auth_required('token')
    @marshal_with(category)
    def get(self):
        cat_list = db.session.query(Category).all()
        return cat_list, 200


class ServiceList(Resource):
    @auth_required('token')
    @marshal_with(service)
    def get(self):
        services = db.session.query(Service).all()
        return services, 200




    @auth_required('token')
    @marshal_with(service)
    def get(self, cat_id):
        services = db.session.query(Service).filter(Service.cat_id == cat_id).all()
        
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
    


# Unauthenticated resource
class UnauthServiceList(Resource):
    @marshal_with(service)
    def get(self):
        services = db.session.query(Service).all()
        return services, 200

