from flask import current_app as app, jsonify
from flask_security import auth_required, SQLAlchemyUserDatastore, verify_password, hash_password
from flask_restful import Resource, fields, marshal_with, reqparse, abort


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
            abort(400, error = "Email is missing")
        
        if password is None:
            abort(400, error = "Password is missing")
        
        user = ds.find_user(email = email)

        if (not user):
            abort(404, error = "Invalid Credentials")
        
        if(verify_password(password, user.password)):
            user.token = user.get_auth_token()
            return user, 200
        else:
            abort(404, error = "Invalid Credentials")
            
    

    



    