from django import forms

from ..models.drug_disposal import DrugDisposalUpload


class DrugDisposalUploadForm(forms.ModelForm):
    class Meta:
        models = DrugDisposalUpload
        fields = '__all__'
