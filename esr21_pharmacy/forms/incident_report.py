from django import forms

from esr21_pharmacy.models import IncidentReportUpload


class IncidentReportUploadForm(forms.ModelForm):
    class Meta:
        models = IncidentReportUpload
        fields = '__all__'
