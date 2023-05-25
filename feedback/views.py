from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import FeedBack
from doctor.models import Doctor
import json
from rest_framework.renderers import JSONRenderer




def addFeedback(request):
    if request.method == 'POST':
        user = FeedBack()
        doctor = Doctor.objects.filter(id=request.POST.get('doctorId'))[0]
        print("==============")
        print(doctor)
        print("==============")
        user.userName = request.POST.get('userName')
        user.userEmail = request.POST.get('userEmail')
        user.doctorId = request.POST.get('doctorId')
        user.doctorName = 'Dr.'+doctor.name+ " " +doctor.lname
        user.rating = request.POST.get('rating')
        user.description = request.POST.get('description')
        user.viwedByDoctor = request.POST.get('viwedByDoctor')
        user.viwedByAdmin = request.POST.get('viwedByAdmin')
        user.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    

def getFeedback(request, doctorId):
    if request.method == 'GET':
        my_list = []
        result =  FeedBack.objects.filter(doctorId=doctorId)
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['userName'] = data.userName
            Dict['userEmail'] = data.userEmail
            Dict['doctorName'] = data.doctorName
            Dict['doctorId'] = data.doctorId
            Dict['rating'] = data.rating
            Dict['description'] = data.description
            Dict['viwedByDoctor'] = data.viwedByDoctor
            Dict['viwedByAdmin'] = data.viwedByAdmin
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    
    

def FeedBackApi(request, doctorId):
    if request.method == 'GET':
        my_list = []
        result =  FeedBack.objects.filter(doctorId=doctorId)
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['userName'] = data.userName
            Dict['userEmail'] = data.userEmail
            Dict['doctorId'] = data.doctorId
            Dict['rating'] = data.rating
            Dict['description'] = data.description
            Dict['viwedByDoctor'] = data.viwedByDoctor
            Dict['viwedByAdmin'] = data.viwedByAdmin
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    if request.method == 'POST':
        user = FeedBack()
        user.userName = request.POST.get('userName')
        user.userEmail = request.POST.get('userEmail')
        user.doctorId = request.POST.get('doctorId')
        user.rating = request.POST.get('rating')
        user.description = request.POST.get('description')
        user.viwedByDoctor = request.POST.get('viwedByDoctor')
        user.viwedByAdmin = request.POST.get('viwedByAdmin')
        user.save()
        return HttpResponse(json.dumps({"code": 201}, ensure_ascii=False), content_type='application/json')
    

class FeedBackApiGeneral(APIView):
    @csrf_exempt
    def get(self, request):
        my_list = []
        result =  FeedBack.objects.all()
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['userName'] = data.userName
            Dict['userEmail'] = data.userEmail
            Dict['doctorId'] = data.doctorId
            Dict['rating'] = data.rating
            Dict['doctorName'] = data.doctorName
            Dict['description'] = data.description
            Dict['viwedByDoctor'] = data.viwedByDoctor
            Dict['viwedByAdmin'] = data.viwedByAdmin
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    


def renderUserFeedback(request):
    return render(request, "feedbackUser.html")

def renderDoctorFeedback(request):
    return render(request, "doctorFeedback.html")
