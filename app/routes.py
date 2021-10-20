from flask import jsonify

from app import app
from app.views import users, authentication, blog


@app.get("/")
@authentication.token_required
def index(**kwargs):
    return jsonify({"message": f"Welcome {kwargs['user'].get_full_name()}!"})


@app.post("/users")
def post_user():
    return users.post_user()


@app.get("/users/<pk>")
def get_user(pk):
    return users.get_user(pk)


@app.post("/get-token")
def get_token():
    return authentication.get_token()


@app.post("/posts")
@authentication.token_required
def add_post(**kwargs):
    return blog.create_post(**kwargs)


@app.delete("/posts/<int:pk>")
@authentication.token_required
def delete_post(pk, **kwargs):
    return blog.delete_post(pk=pk, **kwargs)


@app.post("/comments")
@authentication.token_required
def post_comment(**kwargs):
    return blog.post_comment(**kwargs)


@app.delete("/comments/<int:pk>")
@authentication.token_required
def delete_comment(pk, **kwargs):
    return blog.delete_comment(pk, **kwargs)
