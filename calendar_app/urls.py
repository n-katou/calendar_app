from django.urls import path
from . import views
from .views import list, detail, create, calendar


app_name = "cal"
urlpatterns = [
    path("sc/", views.calendar, name='calendar'),
    # path('sc/', calendar.as_view(), name="calendar"),
    path('list/', list.as_view(), name='list'),
    path('detail/<int:pk>', detail.as_view(), name='detail'),
    path('create/', create.as_view(), name='create'),
]