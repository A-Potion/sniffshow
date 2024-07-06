from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/",
    auth_views.LoginView.as_view(next_page="event:add"), name="login",
    ),
    path("logout/",
    auth_views.LogoutView.as_view(next_page="event:list"), name="logout",
    ),
    path("signup", views.signup, name="signup"),
    path("profile", views.profile, name="profile"),
    path('', include('django.contrib.auth.urls')),
]
