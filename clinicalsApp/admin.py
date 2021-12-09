from django.contrib import admin
from clinicalsApp.models import Patient, ClinicalData
# Register your models here.

# class PatientAdmin(admin.ModelAdmin):
#     list_display = ['id', 'firstName', 'lastName', 'salary', 'email']

class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'ssn', 'age']

class ClinicalDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'componentName', 'componentValue', 'measuredDateTime', 'patient_id']

admin.site.register(Patient, PatientAdmin)
admin.site.register(ClinicalData, ClinicalDataAdmin)



