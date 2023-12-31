from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .manual_auth import CustomAuth
from .utilities import get_user_object


class EndpointsView(APIView):
    def get(self, request):
        data = {
            'register_user': '/api/register/',
            'login': '/api/token/',
            'refresh_token': '/api/tokenrefresh/',
            'logout': '/api/logout/',
            'protected_class_view': '/api/protected-class/',
            'protected_function_view': '/api/protected-function/',
            'user_profile': '/api/user/',
        }
        return Response(data)
    


class UserProfile(APIView):
    permission_classes = [CustomAuth]

    def get(self, request):
        user = get_user_object(request.COOKIES.get("access_token"))
        data = {
            # user info to be stored in react state
            'message': 'This the user profile.',
            'email': user.email,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'is_admin':user.is_admin,
        }
        return Response(data)




@api_view(['GET'])
@permission_classes([CustomAuth])
def protected_view(request):
    print("In protect function view")
    data = {
        'message': 'This is a protected function view.',
    }
    return Response(data)





class ProtectedClassView(APIView):
    permission_classes = [CustomAuth]

    def get(self, request):
        print("In ProtectedClassView")
        data = {
            'message': 'This is a protected class view.',
        }
        return Response(data)