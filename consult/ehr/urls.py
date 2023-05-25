from django.urls import path
from . import views

urlpatterns=[
    path('upload', views.uploadTest, name='upload_file'),
    path('add', views.addEhrRequest),
    path('accept/<int:id>', views.acceptEhrRequest),
    path('check/<str:email>', views.getdetialsByEmailId),
    path('list', views.getPendingEhrRequests),
]