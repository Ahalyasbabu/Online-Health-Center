from django.urls import path
from . import views

urlpatterns=[
    path('', views.departments, name='departments'),
    path('api/departmnet', views.DepartmentAPi.as_view()),
    path('api/all', views.DepartmentGeneral.as_view()),
    path('api/add', views.addDepartment),
    path('api/delete/<int:id>', views.deleteDepartment),
    path('api/get/<int:id>', views.getDepartment),
    path('api/update', views.updateDepartmnet),
    path('api/getall', views.getAll),
]