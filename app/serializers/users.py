from app import ma


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'created_at')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
