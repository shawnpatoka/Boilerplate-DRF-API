from django.urls import path, include
from .views import protected_view, ProtectedClassView, EndpointsView
from .auth_views import CustomTokenObtainPairView, CustomRefreshTokenView

urlpatterns = [
    # endpoint list
    path('', EndpointsView.as_view(), name='endpoints'),

    # token
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),

    # user accounts
    path('', include('accounts.urls')),

    # protected views
    path('protected-class/', ProtectedClassView.as_view(), name='protected-class-view'),
    path('protected-function/', protected_view, name='protected-view'),
]