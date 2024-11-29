from flask import current_app as app, jsonify, request, send_file
from flask_security import auth_required, SQLAlchemyUserDatastore, verify_password, hash_password, current_user
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from application.database import db
from application.models import Customer, User, ServiceProfessional, Category, Service, ServiceRequest
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from application.celery.tasks import create_sr_csv
from celery.result import AsyncResult
import base64


ds : SQLAlchemyUserDatastore = app.security.datastore

CATEGORY_UPLOAD_FOLDER = 'static/service_category'
SERVICE_UPLOAD_FOLDER = 'static/service'
SP_IMAGE_UPLOAD_FOLDER = 'static/sp/image'
SP_DOC_UPLOAD_FOLDER = 'static/sp/doc'
EXTENSIONS = {'png', 'jpg', 'gif', 'jpeg'}
DOC_EXTENSIONS = {'pdf'}
app.config['CATEGORY_UPLOAD_FOLDER'] = CATEGORY_UPLOAD_FOLDER
app.config['SERVICE_UPLOAD_FOLDER'] = SERVICE_UPLOAD_FOLDER
app.config['SP_IMAGE_UPLOAD_FOLDER'] = SP_IMAGE_UPLOAD_FOLDER
app.config['SP_DOC_UPLOAD_FOLDER'] = SP_DOC_UPLOAD_FOLDER

cache = app.cache

# @app.get('/cache')
# @cache.cached(timeout = 10)
# def check_cache():
#     return str(datetime.now())






@auth_required('token')
@app.get('/celery/create_sr_export_request')
def create_export_sr_task():
    task = create_sr_csv.delay()
    return {'task_id': task.id}, 200

@auth_required('token')
@app.get('/celery/create_sp_sr_export_request/<int:sp_id>')
def create_export_sp_sr_task(sp_id):
    task = create_sr_csv.delay(sp_id)
    return {'task_id': task.id}, 200



@app.get('/celery/check_sr_export/<id>')
def check_sr_export(id):
    result = AsyncResult(id)
    if(result.ready()):
        return {'status' : 'ready'}, 200
    else:
        return {'status' : 'not ready'}, 405
    
@app.get('/celery/get_sr_export/<id>')
def get_sr_export(id):
    result = AsyncResult(id)
    if(result.ready()):
        return send_file(result.result)
    else:
        return {'status' : 'not ready'}, 405
    

@app.post('/admin/download')
def download_file():
    check_admin_role()
    data = request.get_json()
    file_path = data.get("submitted_doc_path")
    return send_file(file_path)



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


# Customer Update Parser
customer_update_parser = reqparse.RequestParser()
customer_update_parser.add_argument("f_name")
customer_update_parser.add_argument("l_name")
customer_update_parser.add_argument("address")
customer_update_parser.add_argument("loc_pincode")
customer_update_parser.add_argument("description")
customer_update_parser.add_argument("active", required=False)


# SP Update Parser
sp_update_parser = reqparse.RequestParser()
sp_update_parser.add_argument("f_name")
sp_update_parser.add_argument("l_name")
sp_update_parser.add_argument("address")
sp_update_parser.add_argument("loc_pincode")
sp_update_parser.add_argument("price")
sp_update_parser.add_argument("description")
sp_update_parser.add_argument("active", required=False)
sp_update_parser.add_argument("verified", required=False)
sp_update_parser.add_argument("verification_status", required=False)


# Service Request Parser
sr_parser = reqparse.RequestParser()
sr_parser.add_argument("s_id")
sr_parser.add_argument("c_id")
sr_parser.add_argument("sp_id")
sr_parser.add_argument("description")
sr_parser.add_argument("status")
sr_parser.add_argument("address", required=False)
sr_parser.add_argument("remarks", required=False)
sr_parser.add_argument("rating", required=False)
sr_parser.add_argument("date", required=False)

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
    "loc_pincode": fields.String,
    
    }

admin = {
    "uid": fields.Integer,
    "email": fields.String, 
}



category = {
    "cat_id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "thumbnail_url": fields.String,
    "thumbnail": fields.String(default=None)
}

service = {
    "s_id": fields.Integer,
    "name": fields.String,
    "base_price": fields.Integer,
    "req_time": fields.Float,
    "description": fields.String,
    "cat_id": fields.Integer,
    "base_price": fields.Integer,
    "category": fields.Nested(category),
    "thumbnail": fields.String(default=None)
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
    "remarks": fields.String,
    "customer_name": fields.String,
    "customer": fields.Nested(customer),
    "service_name": fields.String,
    "professional_name": fields.String,
    "professional_price": fields.Integer,
    "rating": fields.Integer,
    "service": fields.Nested(service),
    "address": fields.String
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
    "rating": fields.Float,
    "service": fields.Nested(service),
    "service_requests": fields.List(fields.Nested(service_request)),
    "address": fields.String,
    "loc_pincode": fields.Integer,
    "submitted_doc_path": fields.String(default=None),
    "verification_status": fields.String

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
            if(not user.active):
                abort(401, message = "User is blocked")
            if('service_professional' in user.roles):
                sp = db.session.query(ServiceProfessional).filter(ServiceProfessional.sp_id == user.uid).first()
                if(sp.verification_status == 'Pending'):
                    abort(401, message = "Your Application is under verification")
                elif(sp.verification_status == 'Rejected'):
                    abort(401, message = "Your Application is rejected")
            
            user.token = user.get_auth_token()
            return user, 200
        else:
            abort(404, message = "Invalid Credentials")
            
    
class Register(Resource):

    def post(self):
        pass

    
class CustomerResource(Resource):
    @auth_required('token')
    @cache.cached(timeout = 5, key_prefix='customer_cache' )
    @marshal_with(customer)
    def get(self):
        current_customer = db.session.query(Customer).filter(Customer.c_id == current_user.uid).first()
        if not current_customer:
            abort(404, message = "Customer not found")
        current_customer.email = current_user.email
        current_customer.active = current_user.active
        return current_customer, 200
    
    def post(self):
        cache.delete('customer_cache')
        args = customer_parser.parse_args()
        f_name = args.get("f_name", None)
        l_name = args.get("l_name", None)
        email = args.get("email", None)
        password = args.get("password", None)
        if(not f_name):
            abort(400, message = "First Name is missing")
        if(not email):
            abort(400, message = "Email is missing")
        if(not password):
            abort(400, message = "Password is missing")

        customer = ds.find_user(email = email)

        if(customer):
            abort(400, message = "User with the email already exists")

        ds.create_user(email = email, password = hash_password(password), roles = ['customer'])
        customer_user = ds.find_user(email = email)
        customer_data = Customer(c_id = customer_user.uid, f_name = f_name, l_name = l_name, email = email )
        db.session.add(customer_data)
        db.session.commit()

        return "Registration Successful", 200
    
    @auth_required('token')
    def put(self, c_id=None):
        cache.delete('customer_cache')
        args = customer_update_parser.parse_args()
        f_name = args.get("f_name", None)
        l_name = args.get("l_name", None)
        address = args.get("address", None)
        loc_pincode = args.get("loc_pincode", None)
        description = args.get("description", None)
        active = args.get("active", None)
        if(not f_name):
            abort(400, message = "First Name is missing")
        

        

        if c_id is None:
            customer = ds.find_user(email = current_user.email)
            customer_data = db.session.query(Customer).filter(Customer.c_id == current_user.uid).first()
        else:
            check_admin_role()
            customer = ds.find_user(uid = c_id)
            customer_data = db.session.query(Customer).filter(Customer.c_id == c_id).first()

        if active is not None:
            
            if active == 'block':
                check_admin_role()
                customer.active = False
            if active == 'unblock':
                check_admin_role()
                customer.active = True
                
            

        if(not customer):
            abort(400, message = "Customer not found")

        
       

        customer_data.f_name = f_name
        customer_data.l_name = l_name
        customer_data.address = address
        customer_data.loc_pincode = loc_pincode
        customer_data.description = description
        db.session.add(customer)
        db.session.add(customer_data)
        db.session.commit()

        return "Customer Successfully Updated", 200
    
    @auth_required('token')
    def delete(self, c_id):
        cache.delete('customer_cache')
        check_admin_role()
        
        customer = db.session.query(Customer).filter(Customer.c_id == c_id).first()
        customer_user = db.session.query(User).filter(User.uid == customer.c_id).first()
        if customer.profile_image_path:
            os.remove(customer.profile_image_path)
        db.session.delete(customer)
        db.session.delete(customer_user)
        db.session.commit()

        return "Successfully Deleted", 200





class CustomerAddress(Resource):
    @auth_required('token')
    def put(self):
        cache.delete('customer_cache')
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
    @cache.cached(timeout = 5, key_prefix='admin_cache' )
    @marshal_with(admin)
    def get(self):
        check_for_role()
        admin = current_user
        if not admin:
            abort(404, message = "Admin not found")
        return admin, 200
    

class SPResource(Resource):
    @auth_required('token')
    @cache.cached(timeout = 5, key_prefix='sp_cache')
    @marshal_with(sp)
    def get(self):
        current_sp = db.session.query(ServiceProfessional).filter(ServiceProfessional.sp_id == current_user.uid).first()
        rel_service = db.session.query(Service).filter(Service.s_id == current_sp.service_type).first()
        rel_srs = current_sp.srs
        rating_c = 0
        rating_s = 0
        current_sp.rating = 0
        for sr in rel_srs:
            if(sr.status == 'Completed'):
                rating_c += 1
                rating_s += sr.rating
        if(rating_c > 0):
            current_sp.rating = rating_s/rating_c



        current_sp.service = rel_service
        current_sp.service_requests = rel_srs
        if not current_sp:
            abort(404, message = "Service Professional not found")
        return current_sp, 200
    

    def post(self):
        cache.delete('sp_cache')
        cache.delete_memoized(SPList.get)
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        email = request.form.get('email')
        password = request.form.get('password')
        service_type = request.form.get('service_type')
        price = request.form.get('price')
        experience = request.form.get('experience')
        address = request.form.get('address')
        loc_pincode = request.form.get('loc_pincode')
        
        submitted_doc_path = None

        submitted_doc = request.files.get('submitted_doc')
        


        if(not f_name):
            abort(400, message = "First Name is missing")
        if(not email):
            abort(400, message = "Email is missing")
        if(not password):
            abort(400, message = "Password is missing")
        if(not service_type):
            abort(400, message = "service_type is missing")
        if(not price):
            abort(400, message = "price is missing")
        if(not experience):
            abort(400, message = "experience is missing")
        if(not address):
            abort(400, message = "address is missing")
        if(not loc_pincode):
            abort(400, message = "loc_pincode is missing")


        if(not submitted_doc):
            abort(400, message = "submitted_doc is missing")
        
        

        

        sp = ds.find_user(email = email)

        if(sp):
            abort(400, message = "User with the email already exists")

        

        if submitted_doc.filename.split('.')[1].lower() in DOC_EXTENSIONS:
            path = os.path.join(app.config['SP_DOC_UPLOAD_FOLDER'], secure_filename(email + '.' + submitted_doc.filename.split('.')[1].lower()))
            submitted_doc.save(path)
            submitted_doc_path = path

        ds.create_user(email = email, password = hash_password(password), roles = ['service_professional'])
        sp_user = ds.find_user(email = email)
        sp_data = ServiceProfessional(sp_id = sp_user.uid, f_name = f_name, l_name = l_name, email = email, service_type = service_type, price = price, experience = experience, submitted_doc_path = submitted_doc_path, address = address, loc_pincode = loc_pincode )
        db.session.add(sp_data)
        db.session.commit()

        return "Registration Successful", 200
    



    @auth_required('token')
    def put(self, sp_id=None):
        cache.delete('sp_cache')
        cache.delete_memoized(SPList.get)
        args = sp_update_parser.parse_args()
        f_name = args.get("f_name", None)
        l_name = args.get("l_name", None)
        address = args.get("address", None)
        price = args.get("price", None)
        loc_pincode = args.get("loc_pincode", None)
        description = args.get("description", None)
        active = args.get("active", None)
        verified = args.get("verified", None)
        verification_status = args.get("verification_status", None)
        if(not f_name):
            abort(400, message = "First Name is missing")
        
        
        

        if sp_id is None:
            sp = ds.find_user(email = current_user.email)
            sp_data = db.session.query(ServiceProfessional).filter(ServiceProfessional.sp_id == current_user.uid).first()
        else:
            check_admin_role()
            sp = ds.find_user(uid = sp_id)
            sp_data = db.session.query(ServiceProfessional).filter(ServiceProfessional.sp_id == sp_id).first()

        if(not sp):
            abort(400, message = "SP not found")
        
        
        
        
        if active is not None:
            
            if active == 'block':
                check_admin_role()
                sp.active = False
            if active == 'unblock':
                check_admin_role()
                sp.active = True

        if not sp_data.verified:
            check_admin_role()
            if verified == 'verified':
                sp_data.verified = True
                sp_data.verification_status = verification_status
            elif verified == 'rejected':
                sp_data.verified = False
                sp_data.verification_status = verification_status


        sp_data.f_name = f_name
        sp_data.l_name = l_name
        sp_data.address = address
        sp_data.loc_pincode = loc_pincode
        sp_data.description = description
        sp_data.price = price
        db.session.add(sp)
        db.session.add(sp_data)
        db.session.commit()

        return "Professional Successfully Updated", 200
    

    @auth_required('token')
    def delete(self, sp_id):
        cache.delete('customer_cache')
        check_admin_role()
        
        sp = db.session.query(ServiceProfessional).filter(ServiceProfessional.sp_id == sp_id).first()
        sp_user = db.session.query(User).filter(User.uid == sp.sp_id).first()
        if sp.profile_image_path:
            os.remove(sp.profile_image_path)
        if sp.submitted_doc_path:
            os.remove(sp.submitted_doc_path)
        db.session.delete(sp)
        db.session.delete(sp_user)
        db.session.commit()

        return "Successfully Deleted", 200
    


    

class SPList(Resource):
    @auth_required('token')
    @cache.memoize(timeout = 5 )
    @marshal_with(sp)
    def get(self, s_id ):

        if s_id == 0:
            splist = db.session.query(ServiceProfessional).all()
        else:
            splist = db.session.query(ServiceProfessional).filter(ServiceProfessional.service_type == s_id).all()
        if(not splist):
            abort(404, message = "No Service Professional found")
        for sp in splist:
            sp.email = db.session.query(User).filter(User.uid == sp.sp_id).first().email
            sp.active = db.session.query(User).filter(User.uid == sp.sp_id).first().active

            rel_srs = sp.srs
            sp.service_requests = sp.srs
            rating_c = 0
            rating_s = 0
            sp.rating = 0
            for sr in rel_srs:
                if(sr.status == 'Completed'):
                    rating_c += 1
                    rating_s += sr.rating
            if(rating_c > 0):
                sp.rating = rating_s/rating_c
        return splist, 200
    
    
        
        



class CategoryResource(Resource):
    @auth_required('token')
    @cache.memoize(timeout = 5)
    @marshal_with(category)
    def get(self, cat_id ):
        cat = db.session.query(Category).filter(Category.cat_id == cat_id).first()
        if not cat:
            abort(404, message = "Category not found")
        if(cat.thumbnail_url):
            thumbnail = open(cat.thumbnail_url, "rb")
            encoded_thumbnail = base64.b64encode(thumbnail.read()).decode('utf-8')
            cat.thumbnail = encoded_thumbnail
            thumbnail.close()
        return cat, 200
    
    @auth_required('token')
    def put(self, cat_id):
        cache.delete_memoized(CategoryResource.get)
        name = request.form.get('name')
        description = request.form.get('description')
        thumbnail = None
        if request.files:
            thumbnail = request.files.get('thumbnail')
        thumbnail_path = None

        if(not name):
            abort(400, message = "Name is missing")
        if(not description):
            abort(400, message = "Description is missing")
        
        category = db.session.query(Category).filter(Category.cat_id == cat_id).first()

        if not category:
            abort(404, message = "Category Not Found")

        if thumbnail:

            if thumbnail.filename.split('.')[1].lower() in EXTENSIONS:
                path = os.path.join(app.config['CATEGORY_UPLOAD_FOLDER'], secure_filename(name + '.' + thumbnail.filename.split('.')[1].lower()))
                thumbnail.save(path)
                thumbnail_path = path
        else:
            thumbnail_path = category.thumbnail_url
        
        category.name = name
        category.description = description
        category.thumbnail_url = thumbnail_path

        db.session.add(category)
        db.session.commit()

        return "Category successfully updated", 200
    

    @auth_required('token')
    def post(self):
        cache.delete_memoized(CategoryResource.get)
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
            path = os.path.join(app.config['CATEGORY_UPLOAD_FOLDER'], secure_filename(name + '.' + thumbnail.filename.split('.')[1].lower()))
            thumbnail.save(path)
            thumbnail_path = path

        category = Category(name = name, description = description, thumbnail_url = thumbnail_path)

        db.session.add(category)
        db.session.commit()

        return "Category successfully created", 200
    

    @auth_required('token')
    def delete(self, cat_id):
        cache.delete_memoized(CategoryResource.get)
        category = db.session.query(Category).filter(Category.cat_id == cat_id).first()
        os.remove(category.thumbnail_url)
        db.session.delete(category)
        db.session.commit()

        return "Successfully Deleted", 200



        






class ServiceResource(Resource):

    @auth_required('token')
    @marshal_with(service)
    def get(self, s_id):
        service = db.session.query(Service).filter(Service.s_id == s_id).first()
        if not service:
            abort(404, message = "Service not found")
        

        if(service.thumbnail_url):
            thumbnail = open(service.thumbnail_url, "rb")
            encoded_thumbnail = base64.b64encode(thumbnail.read()).decode('utf-8')
            service.thumbnail = encoded_thumbnail
            thumbnail.close()
        
        return service, 200







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
    def put(self, s_id):
        check_admin_role()
        name = request.form.get('name')
        base_price = request.form.get('base_price')
        req_time = request.form.get('req_time')
        description = request.form.get('description')
        cat_id = request.form.get('cat_id')
        thumbnail = None
        if request.files:
            thumbnail = request.files.get('thumbnail')

        thumbnail_path = None



        
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

        if not service:
            abort(404, message = "Service Not Found")


        if thumbnail:


            if thumbnail.filename.split('.')[1].lower() in EXTENSIONS:
                path = os.path.join(app.config['SERVICE_UPLOAD_FOLDER'], secure_filename(name + '.' + thumbnail.filename.split('.')[1].lower()))
                thumbnail.save(path)
                thumbnail_path = path
        
        else:
            thumbnail_path = service.thumbnail_url

        

        service.name = name
        service.base_price = base_price
        service.req_time = req_time
        service.description = description
        service.cat_id = cat_id
        service.thumbnail_url = thumbnail_path

        # if(_method == 'POST'):
        #     service = Service(s_id = 'abcd', name = name, price = price, req_time = req_time, description = description, cat_id = cat_id)
        #     # handle s_id

        db.session.add(service)
        db.session.commit()

        return "Service successfully updated", 200


class SRResource(Resource):
    @auth_required('token')
    @cache.memoize(timeout = 5)
    @marshal_with(service_request)
    def get(self, sr_id):
        service_request = db.session.query(ServiceRequest).filter(ServiceRequest.sr_id == sr_id).first()
        if not service_request:
            abort(404, message = "SR not found")
        rel_service = db.session.query(Service).filter(Service.s_id == service_request.s_id).first()
        rel_customer = db.session.query(Customer).filter(Customer.c_id == service_request.c_id).first()
        rel_professional = db.session.query(ServiceProfessional).filter(ServiceProfessional.sp_id == service_request.sp_id).first()

        service_request.service_name = rel_service.name
        service_request.customer_name = rel_customer.f_name + ' ' + rel_customer.l_name
        service_request.customer = rel_customer
        service_request.professional_name = rel_professional.f_name + ' ' + rel_professional.l_name
        service_request.professional_price = rel_professional.price
        return service_request, 200
    

    @auth_required('token')
    def post(self):
        cache.delete_memoized(SRResource.get)
        cache.delete_memoized(SRListResource.get)
        args = sr_parser.parse_args()
        s_id = args.get("s_id", None)
        c_id = args.get("c_id", None)
        sp_id = args.get("sp_id", None)
        description = args.get("description", None)
        status = args.get("status", None)
        remarks = args.get("remarks", None)
        rating = args.get("rating", None)
        address = args.get("address", None)
        date = args.get("date", None)
        
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

        if(date):
            date = datetime.strptime(date, '%Y-%m-%d')

        new_sr = ServiceRequest(s_id = s_id, c_id = c_id, sp_id = sp_id, description = description, status = status, remarks = remarks, rating = rating, address = address, request_date = date )
        db.session.add(new_sr)
        db.session.commit()

        return "Service Request Created", 200
    
    @auth_required('token')
    def put(self, sr_id):
        cache.delete_memoized(SRResource.get)
        cache.delete_memoized(SRListResource.get)
        args = sr_parser.parse_args()
        s_id = args.get("s_id", None)
        c_id = args.get("c_id", None)
        sp_id = args.get("sp_id", None)
        description = args.get("description", None)
        status = args.get("status", None)
        remarks = args.get("remarks", None)
        rating = args.get("rating", None)
        date = args.get("date", None)

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


        service_request = db.session.query(ServiceRequest).filter(ServiceRequest.sr_id == sr_id).first()

        if not service_request:
            abort(400, message="Service Request not found")
        
        if service_request.status != 'Completed':
            if status == 'Completed':
                service_request.completion_date = datetime.now()

        if(date):
            date = datetime.strptime(date, '%Y-%m-%d')
        else:
            date = service_request.request_date

        service_request.s_id = s_id
        service_request.c_id = c_id
        service_request.sp_id = sp_id
        service_request.description = description
        service_request.status = status
        service_request.remarks = remarks
        service_request.rating = rating
        service_request.request_date = date

        db.session.add(service_request)
        db.session.commit()

        return "Service Request Updated", 200



class SRListResource(Resource):
    @auth_required('token')
    @cache.memoize(timeout = 5)
    @marshal_with(service_request)
    def get(self, c_id , sp_id):
        
        if c_id == 0:
            if sp_id == 0:

                sr_list = db.session.query(ServiceRequest).all()
                
            
            else:
                sr_list = db.session.query(ServiceRequest).filter(ServiceRequest.sp_id == sp_id).all()
                
        else:
            if sp_id == 0:

                sr_list = db.session.query(ServiceRequest).filter(ServiceRequest.c_id == c_id).all()
                
            else:

                sr_list = db.session.query(ServiceRequest).filter((ServiceRequest.sp_id == sp_id) & (ServiceRequest.c_id == c_id) ).all()
                
        for service_request in sr_list:
            rel_service = db.session.query(Service).filter(Service.s_id == service_request.s_id).first()
            rel_customer = db.session.query(Customer).filter(Customer.c_id == service_request.c_id).first()
            rel_professional = db.session.query(ServiceProfessional).filter(ServiceProfessional.sp_id == service_request.sp_id).first()

            service_request.service_name = rel_service.name
            service_request.customer_name = rel_customer.f_name + ' ' + rel_customer.l_name
            service_request.customer = rel_customer
            service_request.professional_name = rel_professional.f_name + ' ' + rel_professional.l_name
            service_request.professional_price = rel_professional.price


        return sr_list, 200




class CategoryList(Resource):
    @auth_required('token')
    @cache.cached(timeout = 5)
    @marshal_with(category)
    def get(self):
        cat_list = db.session.query(Category).all()
        for cat in cat_list:
            if(cat.thumbnail_url):
                thumbnail = open(cat.thumbnail_url, "rb")
                encoded_thumbnail = base64.b64encode(thumbnail.read()).decode('utf-8')
                cat.thumbnail = encoded_thumbnail
                thumbnail.close()
        return cat_list, 200


class ServiceList(Resource):
    @auth_required('token')
    @cache.memoize(timeout = 5)
    @marshal_with(service)
    def get(self, cat_id):

        if cat_id != 0:
            services = db.session.query(Service).filter(Service.cat_id == cat_id).all()
        else:
            services = db.session.query(Service).all()
        

        for service in services:
            if(service.thumbnail_url):
                thumbnail = open(service.thumbnail_url, "rb")
                encoded_thumbnail = base64.b64encode(thumbnail.read()).decode('utf-8')
                service.thumbnail = encoded_thumbnail
                thumbnail.close()
        
        return services, 200
    

class CustomerList(Resource):
    @auth_required('token')
    @cache.cached(timeout = 5)
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

