from django import forms

from ..models import ChainOfCustody, ChainOfCustodyUpload


class ChainOfCustodyForm(forms.ModelForm):
    class Meta:
        models = ChainOfCustody
        fields = '__all__'


class ChainOfCustodyUploadForm(forms.ModelForm):
    class Meta:
        models = ChainOfCustodyUpload
        fields = '__all__'
