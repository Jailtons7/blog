from werkzeug.security import generate_password_hash

from app import db
from flask import request, jsonify
from app.models.users import Users
from app.serializers.users import user_schema


def post_user():
    data = {
        "password": request.json.get("password"),
        "first_name": request.json.get("first_name"),
        "last_name": request.json.get("last_name"),
        "email": request.json.get("email"),
    }

    if not all(data.values()):
        return jsonify(
            {
                "Error": "Please provide data under a JSON object to post a user.",
                "Required fields": ["password", "first_name", 'last_name', 'email'],
                "Optional fields": []
            }
        ), 400

    pass_from_request = data["password"]
    password = generate_password_hash(pass_from_request)
    data["password"] = password

    try:
        user = Users(**data)
        db.session.add(user)
        db.session.commit()
        data = user_schema.dump(user)
    except Exception as e:
        print(e)
        return jsonify(
            {"Error": "Something went wrong, please, contact the site administration"}
        ), 500

    return jsonify(
        {
            "message": "The user was successfully created!",
            "data": data
        }
    ), 201


def get_user(pk):
    user = Users.query.get(pk)
    if not user:
        return jsonify({"message": "User not found", "data": {}}), 404
    data = user_schema.dump(user)
    return jsonify({"message": "Successfully fetched!", "data": data}), 200
