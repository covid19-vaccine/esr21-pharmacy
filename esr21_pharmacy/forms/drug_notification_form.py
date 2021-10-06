from django import forms

from ..models.drug_notification import DrugNotification


class DrugNotificationForm(forms.ModelForm):
    class Meta:
        models = DrugNotification
        fields = '__all__'
