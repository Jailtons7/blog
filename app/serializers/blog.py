from app import ma


class PostsSchema(ma.Schema):
    class Meta:
        fields = ("id", "text", "image__ext", "image__file_name", "created_at", "user_id")


class CommentsSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "text", "post_id", "created_at")


post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)
