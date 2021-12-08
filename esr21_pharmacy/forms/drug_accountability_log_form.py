from django import forms

from ..models.drug_accountability_log import DrugAccountabilityLog


class DrugAccountabilityLogForm(forms.ModelForm):
    class Meta:
        models = DrugAccountabilityLog
        fields = '__all__'
