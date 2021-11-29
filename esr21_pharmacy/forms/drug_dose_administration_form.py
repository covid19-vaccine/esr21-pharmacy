from django import forms
from ..models.drug_dose_administration import DrugDoseAdministration
from ..models.drug_dose_administration import DosageSpillage


class DrugDoseAdministrationForm(forms.ModelForm):
    class Meta:
        models = DrugDoseAdministration
        fields = '__all__'


class DosageSpillageForm(forms.ModelForm):
    class Meta:
        models = DosageSpillage
        fields = '__all__'
