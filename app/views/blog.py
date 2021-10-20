from flask import request, jsonify

from app import db, file_upload
from app.models.blog import Posts, Comments
from app.serializers.blog import post_schema, comment_schema


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
                "message": "Please provide data under a form-data object to make a Post.",
                "required_fields": ["text"],
                "optional_fields": ["image"]
            }
        ), 400
    try:
        post = Posts(**data)
        post.save()
        data = post_schema.dump(post)
    except Exception as e:
        print(e)
        return jsonify(
            {"message": "Something went wrong, please, contact the site administration"}
        ), 500

    return jsonify(
        {
            "message": "The Post was successfully created!",
            "data": data
        }
    ), 201


def delete_post(pk: int, **kwargs) -> tuple:
    """
    delete a post with the primary key passed as first argument.
    it also deletes image from the media folder, keeping database and static media servers sync.

    :param pk: the post primary key
    :param kwargs:
    :return: a tuple with jsonify object and the status code
    """
    post = Posts.query.get(pk)
    if post is None:
        return jsonify({"message": "Post not found", "data": {}}), 404

    if kwargs["user"].id == post.user_id:
        file_upload.delete_files(post, files=["image"])
        return jsonify({"message": "Post Successfully deleted", "data": {}}), 204
    return jsonify({"message": "Permission denied"}), 403


def post_comment(**kwargs):
    data = {
        "post_id": request.json and request.json.get("post_id"),
        "text": request.json and request.json.get("text"),
        "user_id": kwargs["user"].id,
    }
    if not all(data.values()):
        return jsonify({
            "message": "Please provide data under a json object to make a comment.",
            "required_fields": ["text", "post_id"],
            "optional_fields": []
        }), 400

    post = Posts.query.get(data['post_id'])
    if post is None:
        return jsonify({"message": "impossible to comment a inexistent post", "data": {}}), 400

    try:
        comment = Comments(**data)
        db.session.add(comment)
        db.session.commit()
        data = comment_schema.dump(comment)
    except Exception as e:
        print(e)
        return jsonify(
            {"message": "Something went wrong, please, contact the site administration"}
        ), 500
    return jsonify({"message": "Comment created successfully", "data": data}), 200
