from app import ma


class PostsSchema(ma.Schema):
    class Meta:
        fields = ("id", "text", "image__ext", "image__file_name", "created_at", "user_id")


post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)
