from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import views
from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='sign_up'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/customtoken/',views.CustomTokenObtainPairView.as_view(), name='custom_token'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('userview/',views.UserView.as_view(),name='user_view')
]