from django.urls import path
from . import views
urlpatterns=[
    path('', views.all_doctors, name='doctors'),
    path('doctorHome', views.doctor_appointments, name='doctors-home'),
    path('doctorProfile', views.doctor_profile, name='doctor-profile'),
    path('ehrList', views.patientEhr_details, name='doctor-ehr-list'),
    path('doctors/<int:departmnetId>', views.doctors, name='doctors_by_departments'),
    path('list', views.DoctorGeneral.as_view()),
    path('user/feedback', views.userFeedbackView, name='feedback-add'),
    path('doctors-details/<int:doctorId>', views.doctor_details, name='doctor-details'),
    path('api/doctor/<int:departmentId>', views.DoctorApi.as_view()),
    path('api/profile/<int:id>', views.profileManagement),
    path('api/doctor/<str:email>/<str:password>', views.DoctorAuth.as_view()),
    path('api/add', views.addDoctor),
    path('api/delete/<int:id>', views.deleteDoctor),
    path('api/get/<int:id>', views.getDocotr),
    path('api/update', views.updateProfile),
]