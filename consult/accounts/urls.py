from django.urls import path
from . import views

urlpatterns=[
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('', views.home, name='homepage'),
    path('cadmin', views.adminLogin, name='admin-login'),
    path('cadmin/ehr', views.adminEhrRequests, name='admin-ehr'),
    path('cadmin/home', views.adminHome, name='admin-home'),
    path('cadmin/doctors', views.adminDoctorList, name='admin-doctors'),
    path('cadmin/medicines', views.adminMedicine, name='admin-meds'),
    path('cadmin/appointments', views.adminAppointments, name='admin-appointments'),
    path('cadmin/departments', views.adminDepartments, name='admin-departments'),
    path('cadmin/feedbacks', views.adminFeedbacks, name='admin-feedbacks'),
    path('profile', views.userProfile, name='profile-page'),
    path('doclogin', views.doctorLogin, name='doctor-login'),
    #REST APIs
    path('api/login/<str:email>/<str:password>', views.UserAuthApi.as_view()),
    path('api/register', views.addUser),
    path('api/profile/<str:email>', views.Profile.as_view(), name='uprofile'),
    path('api/profile/update/<str:email>', views.editProfile),
    path('api/get-by-email/<str:email>', views.getUserByEmail)
]