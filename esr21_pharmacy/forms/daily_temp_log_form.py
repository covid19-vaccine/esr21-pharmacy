from django import forms

from ..models import DailyTempLogUpload


class DailTempLogUploadForm(forms.ModelForm):
    class Meta:
        models = DailyTempLogUpload
        fields = '__all__'
