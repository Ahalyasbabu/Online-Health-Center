from django.shortcuts import render

# Create your views here.
def show_medical_reports(request):
    return render(request, 'medicalReports.html')