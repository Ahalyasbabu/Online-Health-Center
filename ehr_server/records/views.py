from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import json
from .models import Records
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt
def addRecord(request):
    if request.method == 'POST':
        r = Records()
        r.ehrId = request.POST.get('ehrId', '')
        r.documentLink = request.POST.get('documentLink', '')
        current_datetime = datetime.now()
        r.created_at = str(current_datetime)
        r.save()
        data = {'code':  201}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    

@csrf_exempt
def getRecords(request, id):
    if request.method == 'GET':
        result = Records.objects.filter(ehrId=id)
        my_list = []
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['ehrId'] = data.ehrId
            Dict['documentLink'] = data.documentLink
            Dict['created_at'] = data.created_at
            my_list.append(Dict)
        json_data = json.dumps(my_list)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
        

