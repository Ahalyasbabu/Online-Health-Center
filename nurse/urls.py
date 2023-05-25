from django.urls import path
from . import views

urlpatterns=[
    path('api/getall', views.getAll),
    path('api/update', views.updateProfile),
    path('api/add', views.addNurse),
    path('api/delete/<int:id>', views.deleteNurse),
    path('api/get/<int:id>', views.getNurse),
    path('nurse', views.renderNurse, name="nurse-page"),
    path('login', views.login, name="nurse-login"),
    path('api/login/<str:email>/<str:password>', views.loginNurse),
    path('home', views.home, name="nurse-home"),
    path('medicineList', views.medicineList, name="nurse-medicineList"),
    path('profile', views.profile, name="nurse-profile")
]   