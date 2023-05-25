from django.urls import path
from . import views

urlpatterns=[
    path('reports', views.show_medical_reports, name="medical-reports"),
]