from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Medicine
import json

class MedicineApi(APIView):
    @csrf_exempt
    def get(self, request):
        my_list = []
        result =  Medicine.objects.all()
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['name'] = data.name
            Dict['price'] = data.price
            Dict['inStock'] = data.inStock
            Dict['provider'] = data.provider
            Dict['manufacturing_date'] = data.manufacturing_date
            Dict['availablity'] = data.availablity
            Dict['description'] = data.description
            Dict['more'] = data.more
            Dict['expiration_date'] = data.expiration_date
            my_list.append(Dict)
        return HttpResponse(json.dumps(my_list, ensure_ascii=False), content_type='application/json')
    
def addMedicine(request):
    if request.method == 'POST':
        medicine = Medicine()
        medicine.name = request.POST.get('name')
        medicine.price = request.POST.get('price')
        medicine.inStock = request.POST.get('inStock')
        medicine.provider = "TBA"
        medicine.manufacturing_date = request.POST.get('manufacturing_date')
        medicine.availablity = "yes"
        medicine.description = "TBA"
        medicine.more = "TBA"
        medicine.expiration_date = request.POST.get('expiration_date')
        medicine.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    

def deleteMedicine(request, id):
    if request.method == 'GET':
        medicine = Medicine.objects.get(id=id)
        medicine.delete()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
    


def getMedicine(request, id):
    if request.method == 'GET':
        m = Medicine.objects.get(id=id)
        Dict = {}
        Dict['name'] = m.name
        Dict['price'] = m.price
        Dict['inStock'] = m.inStock
        Dict['manufacturing_date'] = m.manufacturing_date
        Dict['expiration_date'] = m.expiration_date
        Dict['id'] = m.id
        return HttpResponse(json.dumps(Dict), status=status.HTTP_201_CREATED, content_type='application/json')
    
def updateMedicine(request):
    if request.method == 'POST':
        medicine = Medicine.objects.get(id=request.POST.get('id'))
        medicine.name = request.POST.get('name')
        medicine.price = request.POST.get('price')
        medicine.inStock = request.POST.get('inStock')
        medicine.provider = "TBA"
        medicine.manufacturing_date = request.POST.get('manufacturing_date')
        medicine.availablity = "yes"
        medicine.description = "TBA"
        medicine.more = "TBA"
        medicine.expiration_date = request.POST.get('expiration_date')
        medicine.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')


def medicineList(request):
    return render(request, "medicines.html")



def medicineListDoctor(request):
    return render(request, "doctor-medicines.html")
