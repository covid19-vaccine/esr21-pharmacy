from django import forms

from ..models.drug_requisition import DrugRequisition


class DrugRequisitionForm(forms.ModelForm):
    class Meta:
        models = DrugRequisition
        fields = '__all__'
