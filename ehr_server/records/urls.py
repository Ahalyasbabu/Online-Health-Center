from django.urls import path
from . import views

urlpatterns=[
    path('add', views.addRecord),
    path('get/<str:id>', views.getRecords),
]   