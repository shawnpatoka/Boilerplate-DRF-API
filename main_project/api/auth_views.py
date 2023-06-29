from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data['access']
        refresh_token = response.data['refresh']
        response.set_cookie('access_token', access_token, httponly=True)
        response.set_cookie('refresh_token', refresh_token, httponly=True)
        return response

class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data['access']
        response.set_cookie('access_token', access_token, httponly=True)
        return response
    

