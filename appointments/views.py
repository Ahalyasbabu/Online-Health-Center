from django.shortcuts import render
from departments.models import Departments
from .models import AppointmentsModel
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppointmentSerialiser
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def getAppointments(request, id):
    if request.method == 'GET':
        my_list = []
        result =  AppointmentsModel.objects.filter(userId=id).all()
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['timeSlot'] = data.timeSlot
            Dict['dateSlot'] = data.dateSlot
            Dict['userId'] = data.userId
            Dict['doctorId'] = data.doctorId
            Dict['status'] = data.status
            Dict['doctorName'] = data.doctorName
            Dict['patientName'] = data.patientName
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')

def bookAppointments(request):
    if request.method == 'POST':
        appintment = AppointmentsModel()
        appintment.timeSlot = request.POST.get('timeSlot')
        appintment.dateSlot = request.POST.get('dateSlot')
        appintment.userId = request.POST.get('userId')
        appintment.doctorId = request.POST.get('doctorId')
        appintment.status = request.POST.get('status')
        appintment.doctorName = request.POST.get('doctorName')
        appintment.patientName = request.POST.get('patientName')
        appintment.save()
        return HttpResponse(json.dumps({"code": 201}, ensure_ascii=False), content_type='application/json')

     


class DoctorAppointments(APIView):
    @csrf_exempt
    def get(self, request,id):
        my_list = []
        result =  AppointmentsModel.objects.filter(doctorId=id).all()
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['timeSlot'] = data.timeSlot
            Dict['dateSlot'] = data.dateSlot
            Dict['userId'] = data.userId
            Dict['doctorId'] = data.doctorId
            Dict['status'] = data.status
            Dict['doctorName'] = data.doctorName
            Dict['patientName'] = data.patientName
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    


class AppointmentGeneral(APIView):
    @csrf_exempt
    def get(self, request):
        my_list = []
        result =  AppointmentsModel.objects.filter(status = "booked")
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['timeSlot'] = data.timeSlot
            Dict['dateSlot'] = data.dateSlot
            Dict['userId'] = data.userId
            Dict['doctorId'] = data.doctorId
            Dict['status'] = data.status
            Dict['doctorName'] = data.doctorName
            Dict['patientName'] = data.patientName
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')



    
# Create your views here.
def makeAppointment(request):
    return render(request, 'success.html')


def sucessBooking(request):
    return render(request, 'success.html')


def list_my_appointment(request):
    return render(request, 'Appointments.html')
        
    #return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')


def book_now(request):
     department = Departments.objects.all()
     return render(request, 'date.html', {'departments': department})
