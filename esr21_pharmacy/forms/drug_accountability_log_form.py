from django import forms
from edc_form_validators import FormValidatorMixin

from ..models.drug_accountability_log import DrugAccountabilityLog


class DrugAccountabilityLogForm(FormValidatorMixin, forms.ModelForm):

    class Meta:
        models = DrugAccountabilityLog
        fields = '__all__'
