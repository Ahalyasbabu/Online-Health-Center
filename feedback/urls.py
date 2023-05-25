from django.urls import path
from . import views

urlpatterns=[
    path('user', views.renderUserFeedback, name="user-feedback"),
    path('doctor', views.renderDoctorFeedback, name="doctor-feedback"),
    path('api/doctor/<int:doctorId>', views.FeedBackApi),
    path('api/all', views.FeedBackApiGeneral.as_view()),
    path('api/add', views.addFeedback),
    path('api/doctor/get/<int:doctorId>', views.getFeedback),
    # path('api', views.FeedBackApi)
]