from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validations import DrugAccountabilityLogFormValidator
from ..models.drug_accountability_log import DrugAccountabilityLog


class DrugAccountabilityLogForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = DrugAccountabilityLogFormValidator


    class Meta:
        models = DrugAccountabilityLog
        fields = '__all__'
