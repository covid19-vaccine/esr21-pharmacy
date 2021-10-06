from django import forms

from ..models.drug_disposal import DrugDisposal
from ..models.drug_disposal import Signatures


class DrugDisposalForm(forms.ModelForm):
    class Meta:
        models = DrugDisposal
        fields = '__all__'


class SignaturesForm(forms.ModelForm):
    class Meta:
        models = Signatures
        fields = '__all__'
