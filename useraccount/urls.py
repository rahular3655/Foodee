from django.urls import path
from useraccount.views.auth_vi import UserRegisterView,MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('signup',UserRegisterView.as_view(),name='signup'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
