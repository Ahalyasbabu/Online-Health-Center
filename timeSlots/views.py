from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.core import serializers
from django.http import JsonResponse
import json
from .models import TimeSlots
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class TimeSlotsApi(APIView):
    @csrf_exempt
    def get(self, request):
        my_list = []
        result =  TimeSlots.objects.filter(availability='yes').all()
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['timeSlot'] = data.timeSlot
            Dict['dateSlot'] = data.dateSlot
            print( Dict['timeSlot'])
            my_list.append(Dict)
        print(my_list)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
