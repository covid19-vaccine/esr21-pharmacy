from django import forms

from ..models import ChainOfCustodyUpload


class ChainOfCustodyUploadForm(forms.ModelForm):
    class Meta:
        models = ChainOfCustodyUpload
        fields = '__all__'
