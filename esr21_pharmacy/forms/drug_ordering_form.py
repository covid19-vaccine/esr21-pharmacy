from django import forms

from ..models.drug_ordering import DrugOrdering


class DrugOrderingForm(forms.ModelForm):
    class Meta:
        model = DrugOrdering
        fields = '__all__'
