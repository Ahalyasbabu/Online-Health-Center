from django.shortcuts import render
from .models import Nurse
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import json

# Create your views here.

def addNurse(request):
    if request.method == 'POST':
        nurse = Nurse()
        nurse.name = request.POST.get('name')
        nurse.lname = request.POST.get('lname')
        nurse.qualification = request.POST.get('qualification')
        nurse.availability = True
        nurse.email = request.POST.get('email')
        nurse.password = request.POST.get('password')
        nurse.year_of_experience = request.POST.get('year_of_experience')
        nurse.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')

def getAll(request):
        my_list = []
        nurse =  Nurse.objects.all()
        for data in nurse:
            Dict = {}
            Dict['name'] = data.name
            Dict['lname'] = data.lname
            Dict['qualification'] = data.qualification
            Dict['email'] = data.email
            Dict['year_of_experience'] = data.year_of_experience
            Dict['id'] = data.id
            Dict['availability'] = data.availability
            my_list.append(Dict)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')   

def loginNurse(request, email,  password):
        my_list = []
        result =  Nurse.objects.filter(email=email, password=password)
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['name'] = data.name
            Dict['lname'] = data.lname
            Dict['qualification'] = data.qualification
            Dict['availability'] = data.availability
            Dict['email'] = data.email
            Dict['year_of_experience'] = data.year_of_experience
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list), status=status.HTTP_201_CREATED, content_type='application/json')


def getNurse(request, id):
    if request.method == 'GET':
        nurse = Nurse.objects.get(id=id)
        Dict = {}
        Dict['name'] = nurse.name
        Dict['lname'] = nurse.lname
        Dict['qualification'] = nurse.qualification
        Dict['email'] = nurse.email
        Dict['year_of_experience'] = nurse.year_of_experience
        Dict['id'] = nurse.id
        return HttpResponse(json.dumps(Dict), status=status.HTTP_201_CREATED, content_type='application/json')


def deleteNurse(request, id):
    if request.method == 'GET':
        nurse = Nurse.objects.get(id=id)
        nurse.delete()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    

def updateProfile(request):
    if request.method == 'POST':
        nurse = Nurse.objects.get(id=request.POST.get('id'))
        nurse.name = request.POST.get('name')
        nurse.lname = request.POST.get('lname')
        nurse.email = request.POST.get('email')
        nurse.qualification = request.POST.get('qualification')
        nurse.year_of_experience = request.POST.get('year_of_experience')
        nurse.save()
        res = {}
        res['code'] = 201
        return HttpResponse(json.dumps(res), status=status.HTTP_201_CREATED, content_type='application/json')
    

def renderNurse(request):
    return render(request, "Admin-Nurse.html")

def login(request):
    return render(request, "nurseLogin.html")

def home(request):
    return render(request, "NurseHome.html")

def medicineList(request):
    return render(request, "nurse-medicines.html")

def profile(request):
    return render(request, "NurseProfile.html")