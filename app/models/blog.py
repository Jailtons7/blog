from typing import Optional

from datetime import datetime

from app import db, file_upload


@file_upload.Model
class Posts(db.Model):
    """
    Defines the attributes of posts table in the database
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text())
    image = file_upload.Column()
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("Users", foreign_keys="Posts.user_id")

    def __init__(self, text: str, user_id: int, image: Optional[str] = None):
        self.text = text
        self.user_id = user_id
        self.image = image

    def save(self):
        """
        save the object in the database and return it
        :return: a <Posts object>
        """
        file_upload.save_files(self, files={"image": self.image})
        return self


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text(), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    created_at = db.Column(db.DateTime, default=datetime.now())

    post = db.relationship("Posts", foreign_keys="Comments.post_id")


class Albums(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))

    user = db.relationship("Users", foreign_keys="Albums.user_id")


class ImagesAlbums(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    album_id = db.Column(db.Integer(), db.ForeignKey("albums.id"))

    album = db.relationship("Albums", foreign_keys="ImagesAlbums.album_id")
