from django import forms

from ..models.drug_accountability_log import DrugAccountabilityLog
from ..models.drug_accountability_log import DrugAccountabilityLogInline


class DrugAccountabilityLogForm(forms.ModelForm):
    class Meta:
        models = DrugAccountabilityLog
        fields = '__all__'


class DrugAccountabilityLogInLineForm(forms.ModelForm):
    class Meta:
        models = DrugAccountabilityLogInline
        fields = '__all__'
