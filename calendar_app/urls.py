from django.urls import path
from . import views
from .views import detail, create, calendar, delete, update,get_events


app_name = "cal"
urlpatterns = [
    path("calendar/", views.calendar, name='calendar'),
    path('detail/<int:pk>', detail.as_view(), name='detail'),
    path('create/', create.as_view(), name='create'),
    path('delete/<int:pk>', delete.as_view(), name='delete'),
    path('update/<int:pk>', update.as_view(), name='update'),
    path('get-events/', views.get_events, name='get_events'),
]