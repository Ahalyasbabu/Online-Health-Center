from django.shortcuts import render
from .models import Doctor
from departments.models import Departments 
from django.http import HttpResponse
from .serializers import DoctorSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

import json


class DoctorApi(APIView):
    @csrf_exempt
    def get(self, request, departmentId):
        if request.method == 'GET':
            my_list = []
            result =  Doctor.objects.filter(department=departmentId)
            for data in result:
                Dict = {}
                Dict['name'] = data.name
                Dict['id'] = data.id
                Dict['availability'] = data.availability
                my_list.append(Dict)
            return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    


class DoctorGeneral(APIView):
    @csrf_exempt
    def get(self, request):
        my_list = []
        result =  Doctor.objects.all()
        for data in result:
            Dict = {}
            Dict['name'] = data.name
            Dict['lname'] = data.lname
            Dict['qualification'] = data.qualification
            Dict['email'] = data.email
            Dict['year_of_experience'] = data.year_of_experience
            Dict['department'] = data.department.id
            Dict['id'] = data.id
            Dict['availability'] = data.availability
            my_list.append(Dict)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')

    
class DoctorAuth(APIView):
    @csrf_exempt
    def get(self, request, email,  password):
        my_list = []
        result =  Doctor.objects.filter(email=email, password=password)
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['name'] = data.name
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')


def addDoctor(request):
    if request.method == 'POST':
        department = Departments.objects.get(id=request.POST.get('department'))
        doctor = Doctor()
        doctor.name = request.POST.get('name')
        doctor.lname = request.POST.get('lname')
        doctor.qualification = request.POST.get('qualification')
        doctor.img = request.POST.get('img')
        doctor.availability = True
        doctor.email = request.POST.get('email')
        doctor.password = request.POST.get('password')
        doctor.year_of_experience = request.POST.get('year_of_experience')
        doctor.department = department
        doctor.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')


def getDocotr(request, id):
    if request.method == 'GET':
        doctor = Doctor.objects.get(id=id)
        Dict = {}
        Dict['name'] = doctor.name
        Dict['lname'] = doctor.lname
        Dict['qualification'] = doctor.qualification
        Dict['email'] = doctor.email
        Dict['year_of_experience'] = doctor.year_of_experience
        Dict['id'] = doctor.id
        return HttpResponse(json.dumps(Dict), status=status.HTTP_201_CREATED, content_type='application/json')


def deleteDoctor(request, id):
    if request.method == 'GET':
        doctor = Doctor.objects.get(id=id)
        doctor.delete()

        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')


def updateProfile(request):
    if request.method == 'POST':
        doctor = Doctor.objects.get(id=request.POST.get('id'))
        doctor.name = request.POST.get('name')
        doctor.lname = request.POST.get('lname')
        doctor.email = request.POST.get('email')
        doctor.qualification = request.POST.get('qualification')
        doctor.year_of_experience = request.POST.get('year_of_experience')
        doctor.save()
        res = {}
        res['code'] = 201
        return HttpResponse(json.dumps(res), status=status.HTTP_201_CREATED, content_type='application/json')


def profileManagement(request, id):
    if request.method == 'GET':
        my_list = []
        result =  Doctor.objects.filter(id=id)
        for data in result:
            Dict = {}
            Dict['name'] = data.name
            Dict['lname'] = data.lname
            Dict['qualification'] = data.qualification
            Dict['year_of_experience'] = data.year_of_experience
            Dict['email'] = data.email
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    elif request.method == 'POST':
        doctor = Doctor.objects.get(id=request.POST.get('id'))
        doctor.name = request.POST.get('name')
        doctor.lname = request.POST.get('lname')
        doctor.email = request.POST.get('email')
        doctor.qualification = request.POST.get('qualification')
        doctor.year_of_experience = request.POST.get('year_of_experience')
        doctor.save()
        res = {}
        res['code'] = 201
        return HttpResponse(res, status=status.HTTP_201_CREATED, content_type='application/json')


        


# Create your views here.
def all_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, "doctors.html", {'doctors': doctors})


def doctors(request, departmnetId):
    doctors = Doctor.objects.filter(department=departmnetId)
    return render(request, "doctors.html", {'doctors': doctors})


def doctor_details(request, doctorId):
    doctor = Doctor.objects.filter(department=doctorId)
    return render(request, "date.html", {'doctors': doctor})

def doctor_appointments(request):
    return render(request, "DoctorHome.html")

def doctor_profile(request):
    return render(request, "DoctorProfile.html")


def patientEhr_details(request):
    return render(request, "doctor-ehr.html")


def userFeedbackView(request):
    doctors = Doctor.objects.all()
    return render(request, 'feedback.html',{'doctors': doctors})




