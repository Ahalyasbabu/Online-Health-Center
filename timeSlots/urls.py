from django.urls import path
from . import views
urlpatterns=[
    path('api/timeslot', views.TimeSlotsApi.as_view()),
]