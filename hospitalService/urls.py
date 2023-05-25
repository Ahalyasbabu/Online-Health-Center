from django.urls import path
from . import views

urlpatterns=[
    path('service', views.service_list, name='service-list'),
    path('api/add', views.addService),
    path('api/list', views.getAll),
    path('api/delete/<int:id>', views.delete),
    path('api/update', views.update),
    path('api/get-one/<int:id>', views.getOne)
]