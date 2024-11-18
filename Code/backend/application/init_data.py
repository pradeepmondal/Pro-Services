from flask import current_app as app
from application.database import db
from flask_security import SQLAlchemyUserDatastore, hash_password
from application.models import Customer, ServiceProfessional, Category, Service, ServiceRequest


with app.app_context():
    db.create_all()

    userdatastore : SQLAlchemyUserDatastore = app.security.datastore

    userdatastore.find_or_create_role(name = 'admin', description = 'Administrator')
    userdatastore.find_or_create_role(name = 'service_professional', description = 'Professional providing service')
    userdatastore.find_or_create_role(name = 'customer', description = 'General user')

    admin = userdatastore.find_user(email = 'admin@proservices.xyz')

    if(not admin):
        userdatastore.create_user(email = 'admin@proservices.xyz', password = hash_password('test'), roles = ['admin'])

    test_cat = db.session.query(Category).filter(Category.name == 'Test Category').first()

    if(not test_cat):
        test_cat = Category(name = 'Test Category', description = 'A test category.')
        db.session.add(test_cat)

    test_service = db.session.query(Service).filter(Service.name == 'Test Service').first()

    if(not test_service):
        test_service_cat = db.session.query(Category).filter(Category.name == 'Test Category').first().cat_id
        test_service = Service(name = 'Test Service', price = 500, req_time = 5, description = 'A test service.', cat_id = test_service_cat)
        db.session.add(test_service)

    test_sp = userdatastore.find_user(email = 'rajesh@example.com')

    if(not test_sp):
        userdatastore.create_user(email = 'rajesh@example.com', password = hash_password('test'), roles = ['service_professional'])
        test_sp = userdatastore.find_user(email = 'rajesh@example.com')
        test_sp_service = db.session.query(Service).filter(Service.name == 'Test Service').first().s_id
        test_sp_data = ServiceProfessional(sp_id = test_sp.uid, f_name = 'Rajesh', l_name = 'Kumar', email= 'rajesh@example.com', description = 'A hardworking test SP.', service_type = test_sp_service, experience = 5, submitted_doc_path = 'static/test', loc_pincode = 110001, address = 'Raj Nagar, Delhi, IN')
        db.session.add(test_sp_data)

    test_customer = userdatastore.find_user(email = 'krish02@example.com')

    if(not test_customer):
        userdatastore.create_user(email = 'krish02@example.com', password = hash_password('test'), roles = ['customer'])
        test_customer = userdatastore.find_user(email = 'krish02@example.com')
        test_customer_data = Customer(c_id = test_customer.uid, f_name = 'Krish', l_name = 'Kumar', email= 'krish02@example.com', description = 'A test user', addresses = [], loc_pincode = 110001)
        db.session.add(test_customer_data)


    
    db.session.commit()

