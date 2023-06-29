from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class EndpointsView(APIView):
    def get(self, request):
        data = {
            'register_user': '/api/register/',
            'login': '/api/token/',
            'refresh_token': '/api/tokenrefresh/',
            'logout': '/api/logout/',
            'protected_class_view': '/api/protected-class/',
            'protected_function_view': '/api/protected-function/',
        }
        return Response(data)
    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    user = request.user
    print("this is the user:",user)
    return Response({'message': f'Hello, {user.email}! This is a protected view.'})





class ProtectedClassView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print("this is the user:", user)
        data = {
            'message': 'This is a protected view.',
            'email': user.email,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'is_admin':user.is_admin,

        }
        return Response(data)