from django.shortcuts import render
from .models import UserAccount
from .serializers import UserDataSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers



class UserAuthApi(APIView):
    @csrf_exempt
    def get(self, request, email, password):
        my_list = []
        result =  UserAccount.objects.filter(email=email, password=password)
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['fname'] = data.fname
            Dict['lname'] = data.lname
            Dict['email'] = data.email
            Dict['password'] = data.password
            Dict['img'] = data.img
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if UserAccount.objects.filter(email=request.data.get('email')).exists():
            return Response({},status=status.HTTP_208_ALREADY_REPORTED)
        data = {
            'fname': request.data.get('fname'),
            'lname': request.data.get('lname'),
            'password': request.data.get('password'),
            'email': request.data.get('email'),
            'img': request.data.get('email')
        }
        serializer = UserDataSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def addUser(request):
    if request.method == 'POST':
        user = UserAccount()
        user.fname =  request.POST.get('fname')
        user.lname= request.POST.get('lname')
        user.password = request.POST.get('password')
        user.email= request.POST.get('email')
        # user.img = request.POST.get('img')
        user.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')



def editProfile(request, email):
    user = UserAccount.objects.get(email=email)
    user.fname = request.POST.get('name')
    user.lname = request.POST.get('lname')
    user.email = request.POST.get('email')
    user.save()
    data = {'code': 200}
    json_data = json.dumps(data)
    return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')


def getUserByEmail(request, email):
    user = UserAccount.objects.get(email=email)
    json_data = serializers.serialize('json', [user])
    return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')



class Profile(APIView):
    @csrf_exempt
    def get(self, request, email):
        my_list = []
        result =  UserAccount.objects.filter(email=email)
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['fname'] = data.fname
            Dict['lname'] = data.lname
            Dict['email'] = data.email
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        user = UserAccount.objects.get(email=request.data.get('email'))
        user.fname = request.data.get('name')
        user.lname = request.data.get('lname')
        user.email = request.data.get('email')
        user.save()
        return Response("", status=status.HTTP_201_CREATED)



# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def doctorLogin(request):
    return render(request, 'doctorLogin.html')


def userProfile(request):
    return render(request,"DoctorProfile.html")


def home(request):
    context = {
        "userLogin": 1,
    }
    return render(request, 'index.html', context)

def userProfile(request):
    return render(request, 'profile.html')



def adminLogin(request):
    return render(request, 'admin-login.html')


def adminHome(request):
    return render(request, 'AdminHome.html')


def adminDoctorList(request):
    return render(request, 'Admin-doctor.html')


def adminMedicine(request):
    return render(request, 'Admin-medicine.html')


def adminDepartments(request):
    return render(request, 'Admin-departments.html')

def adminAppointments(request):
    return render(request, 'Admin-appointments.html')


def adminFeedbacks(request):
    return render(request, 'Admin-feedbacks.html')


def adminEhrRequests(request):
    return render(request, 'Admin-ehrList.html')






