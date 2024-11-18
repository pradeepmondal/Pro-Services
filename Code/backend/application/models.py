from application.database import db
from flask_security import UserMixin, RoleMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    active = db.Column(db.Boolean, nullable = False, default = True)
    fs_uniquifier = db.Column(db.String, unique = True, nullable = False)
    roles = db.Relationship('Role', backref = 'bearers', secondary = 'user_roles')

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    rid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    description = db.Column(db.String)

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    ur_id = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    rid = db.Column(db.Integer, db.ForeignKey('role.rid'))

class ServiceProfessional(db.Model):
    __tablename__ = 'service_professional'
    sp_id = db.Column(db.Integer, db.ForeignKey('user.uid'), primary_key = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.now())
    f_name = db.Column(db.String, nullable = False)
    l_name = db.Column(db.String)
    email = db.Column(db.String, db.ForeignKey('user.email'))
    description = db.Column(db.String)
    service_type = db.Column(db.String, db.ForeignKey('service.s_id'))
    experience = db.Column(db.Integer, nullable = False)
    submitted_doc_path = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    loc_pincode = db.Column(db.Integer, nullable = False)
    rating = db.Column(db.Float) 

class Customer(db.Model):
    __tablename__ = 'customer'
    c_id = db.Column(db.Integer, db.ForeignKey('user.uid'), primary_key = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.now())
    f_name = db.Column(db.String, nullable = False)
    l_name = db.Column(db.String)
    email = db.Column(db.String, db.ForeignKey('user.email'))
    description = db.Column(db.String)
    addresses = db.Column(db.JSON)
    loc_pincode = db.Column(db.Integer)
    

class Service(db.Model):
    __tablename__ = 'service'
    s_id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    req_time = db.Column(db.Float, nullable = False)
    description = db.Column(db.String, nullable = False)
    cat_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'))

class Category(db.Model):
    __tablename__ = 'category'
    cat_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    description = db.Column(db.String, nullable = False)

class ServiceRequest(db.Model):
    __tablename__ = 'service_request'
    sr_id = db.Column(db.Integer, primary_key = True)
    s_id = db.Column(db.String, db.ForeignKey('service.s_id'), nullable = False)
    c_id = db.Column(db.Integer, db.ForeignKey('customer.c_id'), nullable = False)
    sp_id = db.Column(db.Integer, db.ForeignKey('service_professional.sp_id'), nullable = False)
    request_date = db.Column(db.DateTime, nullable = False, default = datetime.now())
    completion_date = db.Column(db.DateTime)
    status = db.Column(db.String, nullable = False)
    remarks = db.Column(db.String)
    



