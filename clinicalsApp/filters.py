import django_filters
from clinicalsApp.models import Patient

class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = '__all__'




