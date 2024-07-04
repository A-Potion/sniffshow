from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView

app_name = "accounts"
urlpatterns = [
    path("login/",
    auth_views.LoginView.as_view(next_page="event:add"), name="login",
    ),
    path("logout/",
    auth_views.LogoutView.as_view(next_page="event:list"), name="logout",
    ),
    path("signup", SignUpView.as_view(), name="signup"),
    path('', include('django.contrib.auth.urls')),
]
