from django.urls import path
from . import views

urlpatterns=[
    path('add', views.addUser),
    path('valid/<str:email>', views.getdetialsByEmailId),
]   