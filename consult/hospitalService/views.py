from django.shortcuts import render
from .models import HospitalServices
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import json



def addService(request):
    if request.method == 'POST':
        service = HospitalServices()
        service.title = request.POST.get('title')
        service.availability = request.POST.get('availability')
        service.Age = request.POST.get('age')
        service.Description = request.POST.get('description')
        service.Date = request.POST.get('date')
        service.Time = request.POST.get('time')
        service.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    

def getAll(request):
        my_list = []
        service =  HospitalServices.objects.all()
        for data in service:
            Dict = {}
            Dict['title'] = data.title
            Dict['availability'] = data.availability
            Dict['Age'] = data.Age
            Dict['Description'] = data.Description
            Dict['Date'] = data.Date
            Dict['id'] = data.id
            Dict['Time'] = data.Time
            my_list.append(Dict)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json') 


def getOne(request, id):
    if request.method == 'GET':
        data = HospitalServices.objects.get(id=id)
        Dict = {}
        Dict['title'] = data.title
        Dict['availability'] = data.availability
        Dict['Age'] = data.Age
        Dict['Description'] = data.Description
        Dict['Date'] = data.Date
        Dict['id'] = data.id
        Dict['Time'] = data.Time
        return HttpResponse(json.dumps(Dict), status=status.HTTP_201_CREATED, content_type='application/json')


def delete(request, id):
    if request.method == 'GET':
        service = HospitalServices.objects.get(id=id)
        service.delete()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    

def update(request):
    if request.method == 'POST':
        service = HospitalServices.objects.get(id=request.POST.get('id'))
        service.title = request.POST.get('title')
        service.availability = request.POST.get('availability')
        service.Age = request.POST.get('Age')
        service.Description = request.POST.get('Description')
        service.Date = request.POST.get('Date')
        service.Time = request.POST.get('time')
        service.save()
        res = {}
        res['code'] = 201
        return HttpResponse(json.dumps(res), status=status.HTTP_201_CREATED, content_type='application/json')



# Create your views here.
def service_list(request):
    services = HospitalServices.objects.all()
    return render(request, 'services.html', {'services': services})
