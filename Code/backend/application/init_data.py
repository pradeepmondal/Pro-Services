from flask import current_app as app
from application.database import db
from flask_security import SQLAlchemyUserDatastore, hash_password


with app.app_context():
    db.create_all()

    userdatastore : SQLAlchemyUserDatastore = app.security.datastore

    userdatastore.find_or_create_role(name = 'admin', description = 'Administrator')
    userdatastore.find_or_create_role(name = 'service_professional', description = 'Professional providing service')
    userdatastore.find_or_create_role(name = 'customer', description = 'General user')

    admin = userdatastore.find_user(email = 'admin@proservices.xyz')

    if(not admin):
        userdatastore.create_user(email = 'admin@proservices.xyz', password = hash_password('test'), roles = ['admin'])

    test_sp = userdatastore.find_user(email = 'rajesh@example.com')

    if(not test_sp):
        userdatastore.create_user(email = 'rajesh@example.com', password = hash_password('test'), roles = ['service_professional'])

    test_customer = userdatastore.find_user(email = 'krish02@example.com')

    if(not test_customer):
        userdatastore.create_user(email = 'krish02@example.com', password = hash_password('test'), roles = ['customer'])

    
    db.session.commit()

