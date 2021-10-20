from flask import request, jsonify

from app import db
from app.models.blog import Posts
from app.serializers.blog import post_schema


def create_post(**kwargs):
    """
    creates a post

    :param kwargs:
        :kwargs['user']: the logged user object

    :return: tuple with jsonify object and the status code
    """
    data = {
        "text": request.form.get("text"),
        "user_id": kwargs["user"].id,
        "image": request.files.get("image")
    }
    if not all(data.values()):
        return jsonify(
            {
                "Error": "Please provide data under a form-data object to make a Post.",
                "Required fields": ["text"],
                "Optional fields": ["image"]
            }
        ), 400
    try:
        post = Posts(**data)
        post.save()
        data = post_schema.dump(post)
    except Exception as e:
        print(e)
        return jsonify(
            {"Error": "Something went wrong, please, contact the site administration"}
        ), 500

    return jsonify(
        {
            "message": "The Post was successfully created!",
            "data": data
        }
    ), 201


def delete_post(pk, **kwargs):
    post = Posts.query.get(pk)
    if post is None:
        return jsonify({"message": "Post not found", "data": {}}), 404

    if kwargs["user"].id == post.user_id:
        db.session.query(Posts).filter(Posts.id == post.id).delete()
        db.session.commit()
        return jsonify({"message": "Post Successfully deleted", "data": {}}), 204
    return jsonify({"message": "Permission denied"}), 403
