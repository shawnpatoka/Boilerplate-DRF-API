import jwt
from accounts.models import User
from main_project import settings


def get_user_object(token):
    secret_key = settings.SECRET_KEY
    jwt.decode(token, secret_key, algorithms=['HS256'])
    decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
    user_id = decoded_token.get('user_id')
    user = User.objects.get(pk=user_id)
    return user
