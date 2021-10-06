from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin import ModelAdminMixin
from ..models.daily_temp_log import DailyTempLog
from ..forms.daily_temp_log_form import DailyTempLogForm
from ..admin_site import esr21_pharmacy_admin


@admin.register(DailyTempLog, site=esr21_pharmacy_admin)
class DailyTempLogAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DailyTempLogForm

    readonly_fields = ('investigator', 'product_name', 'site')

    fieldsets = (
        (None, {
            'fields': (
                'site',
                'investigator',
                'product_name',
                'date',
                'current_temp',
                'initials',
                'comments'
            )
        }), audit_fieldset_tuple
    )
