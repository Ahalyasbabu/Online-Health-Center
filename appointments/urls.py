from django.urls import path
from . import views

urlpatterns=[
    path('appointment', views.makeAppointment, name='make-appointment'),
    path('booknow', views.book_now, name='book-appointment'),
    path('successBooking', views.sucessBooking, name='booking-done'),
    path('api/appointments', views.bookAppointments),
    path('api/appointments/list/<str:id>', views.getAppointments),
    path('all', views.AppointmentGeneral.as_view()),
    # path('api/appointments/<str:id>', views.AppointmentApi.as_view()),
    path('api/doctor/appointments/<str:id>', views.DoctorAppointments.as_view()),
    path('myAppointments', views.list_my_appointment, name='userAppointments')
]