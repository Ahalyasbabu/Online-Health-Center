from django.urls import path
from . import views

urlpatterns=[
    path('all', views.MedicineApi.as_view()),
    path('list', views.medicineList, name="list-medicine"),
    path('doctor-list', views.medicineListDoctor, name="list-medicine-doctor"),
    path('api/add', views.addMedicine),
    path('api/delete/<int:id>', views.deleteMedicine),
    path('api/get/<int:id>', views.getMedicine),
    path('api/update', views.updateMedicine),
]