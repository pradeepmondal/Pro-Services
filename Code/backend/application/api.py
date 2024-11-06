from flask import current_app as app, jsonify
from flask_security import auth_required


@app.get('/')
def welcome():
    return jsonify({'message': 'Welcome to Pro Services API 1.0.0'})

    