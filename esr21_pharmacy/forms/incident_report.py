from django import forms

from esr21_pharmacy.models import IncidentReport, IncidentReportUpload


class IncidentReportForm(forms.ModelForm):
    class Meta:
        models = IncidentReport
        fields = '__all__'


class IncidentReportUploadForm(forms.ModelForm):
    class Meta:
        models = IncidentReportUpload
        fields = '__all__'
