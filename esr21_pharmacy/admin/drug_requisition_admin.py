from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin

from ..models.drug_requisition import DrugRequisition
from ..forms.drug_requisition_form import DrugRequisitionForm
from ..admin_site import esr21_pharmacy_admin


@admin.register(DrugRequisition, site=esr21_pharmacy_admin)
class DrugRequisitionAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugRequisitionForm

    readonly_fields = ('investigator', 'study_product_name', 'units', 'acceptable_temp_range')

    fieldsets = (
        (None, {
            'fields': (
                'injection_site',
                'investigator',
                'date',
                'inventory',
                'study_product_name',
                'units',
                'quantity_order',
                'quantity_issued',
                'batch_number',
                'exp_date',
                'quantity_received',
            )
        }), (
            '', {
                'fields': (
                    'study_product_ordered_by',
                    'title',
                    'ordered_by_date_time',
                )
            }
        ),
        (
            ('', {
                'fields': (
                    'acceptable_temp_range',
                    'delivery_site_temp',
                    'last_dose_temp',
                    'temp_control_during_trans',
                    'transportation_control_comment'
                )
            })
        ),
        audit_fieldset_tuple
    )
