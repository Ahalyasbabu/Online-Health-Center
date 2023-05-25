from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import EHR
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from firebase_admin import credentials, storage, initialize_app
import os
import requests
import datetime
import firebase_admin
import io
import uuid
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileMerger, PdfMerger, PdfReader

# Create your views here.
def getPendingEhrRequests(request):
    if request.method == 'GET':
        my_list = []
        result =  EHR.objects.all()
        for data in result:
            Dict = {}
            Dict['id'] = data.id
            Dict['patient_fname'] = data.patient_fname
            Dict['patient_lname'] = data.patient_lname
            Dict['email'] = data.email
            Dict['ehr_status'] = data.ehr_status
            Dict['ehr_id'] = data.ehr_id
            my_list.append(Dict)
        json_data = json.dumps(my_list)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')
        
    


def addEhrRequest(request):
    if request.method == 'POST':
        inputData = EHR()
        inputData.patient_fname = request.POST.get('fname')
        inputData.patient_lname = request.POST.get('lname')
        inputData.email = request.POST.get('email')
        # inputData.ehr_status = "pending"
        data = {'name': request.POST.get('fname') + request.POST.get('lname'), 'email': request.POST.get('email'), 'hospitalId': 'GHS'}
        response = requests.post('http://localhost:8000/ehr/add', data=data)
        if response.status_code == 201:
            data = response.json()
            inputData.ehr_id = data['ehrId']
            
        inputData.ehr_status = "registerd"
        inputData.save()
        data = {'code': 200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')


def getdetialsByEmailId(request, email):
    if request.method == 'GET':
        data =  EHR.objects.get(email=email)
        Dict = {}
        Dict['id'] = data.id
        Dict['patient_fname'] = data.patient_fname
        Dict['patient_lname'] = data.patient_lname
        Dict['email'] = data.email
        Dict['ehr_status'] = data.ehr_status
        Dict['ehr_id'] = data.ehr_id
        json_data = json.dumps(Dict)
        return HttpResponse(json_data, status=status.HTTP_201_CREATED, content_type='application/json')





def acceptEhrRequest(request, id):
    if request.method == 'GET':
        m = EHR.objects.get(id=id)
        data = {'name': m.patient_fname + m.patient_lname, 'email': m.email, 'hospitalId': 'GHS'}
        response = requests.post('http://localhost:8000/ehr/add', data=data)
        if response.status_code == 201:
            data = response.json()
            m.ehr_id = data['ehrId']
            
        m.ehr_status = "registerd"
        m.save()
        data = {'code': 200}
        return HttpResponse(json.dumps(data), status=status.HTTP_201_CREATED, content_type='application/json')


# # Initialize Firebase Admin SDK
# cred = credentials.Certificate('ehrapp-ahalya-firebase-adminsdk-r4unh-7f97de4946.json')
# firebase_admin.initialize_app(cred, {'storageBucket': 'ehrapp-ahalya.appspot.com'})
# bucket = storage.bucket()

cred = credentials.Certificate('ehrapp-ahalya-firebase-adminsdk-r4unh-7f97de4946.json')
initialize_app(cred, {'storageBucket': 'ehrapp-ahalya.appspot.com'})
bucket = storage.bucket()

def uploadTest(request):
    if request.method == 'POST':
        # Get form data and uploaded image
        name = request.POST.get('name')
        prescription = request.POST.get('prescription')
        description = request.POST.get('description')
        ehrId = request.POST.get('ehrId')
        image = request.FILES.get('image_file')
        
        # Create a PDF file
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 750, "title: {}".format(name))
        p.drawString(100, 700, "prescription: {}".format(prescription))
        p.drawString(100, 650, "description: {}".format(description))
        p.showPage()
        p.save()
        buffer.seek(0)
        
        # Merge PDF file with uploaded image
        pdf_merger = PdfMerger()
        pdf_merger.append(PdfReader(buffer))
        pdf_merger.append(PdfReader(image))
        merged_file = io.BytesIO()
        pdf_merger.write(merged_file)
        merged_file.seek(0)
        
        # Upload merged file to Firebase storage
        merged_file_name = str(uuid.uuid4()) + '.pdf'
        blob = bucket.blob(merged_file_name)
        blob.upload_from_string(merged_file.getvalue(), content_type='application/pdf')
        
        # Get download URL of uploaded file
        url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
        
        # update in ehr server
        data = {'ehrId': ehrId, 'documentLink': url}
        response = requests.post('http://localhost:8000/records/add', data=data)
        if response.status_code == 201:
            data = {'code': 200}
            return HttpResponse(json.dumps(data), status=status.HTTP_201_CREATED, content_type='application/json')
        else:
            return HttpResponse('Error')

    else:
        return HttpResponse('Error')


# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         # Get the file object from the request
#         file = request.FILES['file']

#         # Initialize Firebase app with credentials
#         cred = credentials.Certificate('ehrapp-ahalya-firebase-adminsdk-r4unh-7f97de4946.json')
#         initialize_app(cred, {'storageBucket': 'ehrapp-ahalya.appspot.com'})

#         # Upload file to Firebase storage
#         bucket = storage.bucket()
#         blob = bucket.blob(file.name)
#         blob.upload_from_file(file)

#         # Get the public URL of the uploaded file
#         url = blob.public_url

#         # Return a JSON response with the file URL
#         return JsonResponse({'url': url})
#     else:
#         return JsonResponse({'error': 'Invalid request'})

