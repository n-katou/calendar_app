from django.urls import path
from . import views

app_name = "cal"
urlpatterns = [
    path("sc/", views.index, name="index"),
]