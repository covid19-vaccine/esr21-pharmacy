from django import forms

from ..models.daily_temp_log import DailyTempLog


class DailyTempLogForm(forms.ModelForm):
    class Meta:
        model = DailyTempLog
        fields = '__all__'
