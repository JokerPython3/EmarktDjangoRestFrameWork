from django.conf.urls import handler404
from django.urls import path
from rest_framework_simplejwt.views import (
TokenObtainPairView,TokenVerifyView,TokenRefreshView
)
from .util.views_errros import ViewsError
from .views import Login, Register, Profile
from .views import Logout
from .views import UpdateUsername
from .views import UpdatePassword
urlpatterns = [
    path("api/token/",TokenObtainPairView.as_view(),name="token"),
    path("api/token/verify/",TokenVerifyView.as_view(),name="token_verify"),
    path("api/token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("api/auth/login/",Login.as_view(),name="login"),
    path("api/login/auth/register/",Register.as_view(),name="Regisyer"),
    path("api/logout/auth/atro/s1/ntro/",Logout.as_view(), name="Logout"),
    path("api/auth/update/username/account/",UpdateUsername.as_view(),name="UpdateUsername"),
    path("api/auth/update/password/account/",UpdatePassword.as_view(),name="UpdatePassword"),
    path("api/auth/profile/account/info/",Profile.as_view(),name="Profile")
]
handler404 = ViewsError().get()
handler500 =ViewsError().get()