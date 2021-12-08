from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import esr21_pharmacy_admin
from ..forms.drug_accountability_log_form import DrugAccountabilityLogForm
from ..models.drug_accountability_log import DrugAccountabilityLog


@admin.register(DrugAccountabilityLog, site=esr21_pharmacy_admin)
class DrugAccountabilityLogAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugAccountabilityLogForm

    fieldsets = (
        (None, {
            'fields': (
                'date',
                'site',
                'lot_number',
                'exp_date',
                'requisition_form_number',
                'details',
                'received_or_issued',
                'balance_forward',
                'status',
                'comments'
            )
        }
         ),
        audit_fieldset_tuple

    )
