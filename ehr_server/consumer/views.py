from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import json
from .models import Consumer
import random
import string
from django.views.decorators.csrf import csrf_exempt


def generate_alphanumeric_id(length):
    """Generate a random alphanumeric ID of the specified length."""
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    id = ''.join(random.choices(characters, k=length))
    return id

@csrf_exempt
def addUser(request):
    if request.method == 'POST':
        user = Consumer()
        user.name = request.POST.get('name', '')
        user.email = request.POST.get('email', '')
        user.hospitalId = request.POST.get('hospitalId', '')
        user.ehrId = generate_alphanumeric_id(10)
        user.save()
        data = {'ehrId': user.ehrId}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    

@csrf_exempt
def validateEntry(request, id):
    if request.method == 'GET':
        user = Consumer()
        user.name = request.POST.get('name', '')
        user.email = request.POST.get('email', '')
        user.hospitalId = request.POST.get('hospitalId', '')
        user.ehrId = generate_alphanumeric_id(8)
        user.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')


@csrf_exempt
def getdetialsByEmailId(request, email):
    if request.method == 'GET':
        data =  Consumer.objects.get(email=email)
        Dict = {}
        Dict['id'] = data.id
        Dict['name'] = data.name
        Dict['email'] = data.email
        Dict['ehrId'] = data.ehrId
        Dict['hospitalId'] = data.hospitalId
        json_data = json.dumps(Dict)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')