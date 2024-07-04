from django.urls import path
from . import views

app_name = "event"
urlpatterns = [
    path("add/", views.add, name = "add"),
    path("list/", views.ListView.as_view(), name = "list"),
    path("<int:pk>", views.DetailView.as_view(), name="detail"),
    path('', include('django.contrib.auth.urls')),
]
