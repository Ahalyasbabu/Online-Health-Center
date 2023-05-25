from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Departments
from .serializers import DepartmentSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from timeSlots.models import TimeSlots
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


class DepartmentAPi(APIView):
    @csrf_exempt
    def get(self, request):
        data =  Departments.objects.all()
        serializer = DepartmentSerializers(data=data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DepartmentGeneral(APIView):
    @csrf_exempt
    def get(self, request):
        my_list = []
        result =  Departments.objects.all()
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['name'] = data.name
            Dict['description'] = data.description
            my_list.append(Dict)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    

def getAll(request):
    if request.method == 'GET':
        my_list = []
        result =  Departments.objects.all()
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['name'] = data.name
            Dict['description'] = data.id
            my_list.append(Dict)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')

def addDepartment(request):
    if request.method == 'POST':
        department = Departments()
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        department.img = 'appUploads/default.png'
        department.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    
def deleteDepartment(request, id):
    if request.method == 'GET':
        department = Departments.objects.get(id=id)
        department.delete()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')



def updateDepartmnet(request):
    if request.method == 'POST':
        department = Departments.objects.get(id=request.POST.get('id'))
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        department.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')



def getDepartment(request, id):
    if request.method == 'GET':
        d = Departments.objects.get(id=id)
        Dict = {}
        Dict['name'] = d.name
        Dict['description'] = d.description
        Dict['id'] = d.id
        return HttpResponse(json.dumps(Dict), status=status.HTTP_201_CREATED, content_type='application/json')


def departments(request):
    departmentsList = Departments.objects.all()
    return render(request, 'departments.html', {'departments': departmentsList})
