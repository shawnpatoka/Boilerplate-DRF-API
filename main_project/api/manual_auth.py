import jwt
from jwt.exceptions import InvalidTokenError
from accounts.models import User
from main_project import settings


# manual token auth
def authorize_token(access_token):
    try:
        secret_key = settings.SECRET_KEY
        decoded_token = jwt.decode(access_token, secret_key, algorithms=['HS256'])
        user_id = decoded_token.get('user_id')
        authorized_user = User.objects.get(pk=user_id)
        return authorized_user
    except InvalidTokenError:
        return False