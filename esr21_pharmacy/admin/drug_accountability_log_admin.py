from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, audit_fields

from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import esr21_pharmacy_admin
from ..forms.drug_accountability_log_form import DrugAccountabilityLogForm
from ..models.drug_accountability_log import DrugAccountabilityLog


@admin.register(DrugAccountabilityLog, site=esr21_pharmacy_admin)
class DrugAccountabilityLogAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugAccountabilityLogForm

    radio_fields = {
        'injection_site': admin.VERTICAL,
        'status': admin.VERTICAL
        }

    readonly_fields = ['details', 'balance']

    fieldsets = (
        (None, {
            'fields': (
                'tracking_identifier',
                'date',
                'injection_site',
                'lot_number',
                'exp_date',
                'details',
                'quantity_order',
                'quantity_received',
                'issued',
                'status',
                'comments',
                'balance',
                )
            }
         ),
        audit_fieldset_tuple

        )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj) + audit_fields +
                ('tracking_identifier',))
