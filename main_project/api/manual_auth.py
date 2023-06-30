import jwt
from jwt.exceptions import InvalidTokenError
from accounts.models import User
from main_project import settings
from rest_framework.permissions import BasePermission


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
    


class CustomAuth(BasePermission):
    def has_permission(self, request, view):
        try:
            access_token = request.COOKIES.get("access_token")
            secret_key = settings.SECRET_KEY
            jwt.decode(access_token, secret_key, algorithms=['HS256'])
            decoded_token = jwt.decode(access_token, secret_key, algorithms=['HS256'])
            return True
        except jwt.InvalidTokenError:
            return False