from datetime import datetime, timedelta
from functools import wraps

import jwt
from jwt import encode
from flask import request, jsonify
from werkzeug.security import check_password_hash

from app.models.users import Users
from project.settings import Settings


def get_token():
    auth = request.authorization
    # The username must be the user e-mail
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Login required", "WWW-Authenticate": "Basic Auth with e-mail and password"}), 401

    user = Users.get_user_from_email(auth.username)
    if not user or not check_password_hash(user.password, auth.password):
        return jsonify({"message": "The user is not registered or the password is incorrect.", "data": {}}), 401

    exp = datetime.now() + timedelta(hours=10)
    token = encode(
        {"username": user.email, "exp": exp}, Settings.SECRET_KEY
    )
    return jsonify(
        {"message": "Validated Successfully", "token": token, "exp": exp.strftime("%Y-%m-%d %H:%M:%S %f")}
    )


def token_required(f):
    """
    Verifies if token is present in request and if it's valid.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        bearer_token = request.headers.get("Authorization")
        if not bearer_token:
            return jsonify({"message": "Token not set", "data": {}}), 401

        token = bearer_token.replace("Bearer ", "")
        try:
            data = jwt.decode(token, Settings.SECRET_KEY, algorithms=['HS256'])
            user = Users.get_user_from_email(data.get('username'))
            kwargs['user'] = user
        except Exception as e:
            print(f"Authentication: {str(e)}")
            return jsonify({"message": "Token is invalid or expired", "data": {}}), 401

        return f(*args, **kwargs)
    return decorated
