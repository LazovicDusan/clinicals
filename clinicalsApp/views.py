from tkinter import Pack

from django.shortcuts import render, redirect
from clinicalsApp.models import Patient, ClinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from clinicalsApp.filters import PatientFilter

# Create your views here.

def patientListView(request):
    patients = Patient.objects.all()

    # myFilter = PatientFilter(request.GET)

    # patients = myFilter
    return render(request, 'clinicalsApp/patient_list.html', {'patients': patients})
    # return render(request, 'clinicalsApp/patient_list.html', {'patients': patients})

# class PatientListView(ListView):
#     model = Patient

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index') # after patient was created, this is landing page
    fields = ('firstName', 'lastName', 'ssn', 'age')

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index') # after patient was created, this is landing page
    fields = ('firstName', 'lastName', 'ssn', 'age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index') # after patient was created, this is landing page

# class PatientFilterListView(ListView):
#     model = PatientFilter

@login_required
def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/patient')
    return render(request, 'clinicalsApp/clinicalData_form.html', {'form': form, 'patient': patient})

def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for entry in data:
        if entry.componentName == 'hw':
            heightAndWeight = entry.componentValue.split('/')
            if len(heightAndWeight) > 1:
                heightInMeters = float(heightAndWeight[0])/100
                BMI = float(heightAndWeight[1])/(heightInMeters*heightInMeters)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'bmi'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)
        responseData.append(entry)
    return render(request, 'clinicalsApp/generateReport.html', {'data': responseData})

def home(request):
    return render(request, 'clinicalsApp/home.html')

def login(request):
    return render(request, 'clinicalsApp/registerPage.html')

def register(request):
    return render(request, 'clinicalsApp/registerPage.html')












