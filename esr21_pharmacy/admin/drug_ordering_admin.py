from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin import ModelAdminMixin
from ..admin_site import esr21_pharmacy_admin
from ..forms.drug_ordering_form import DrugOrderingForm
from ..models.drug_ordering import DrugOrdering


@admin.register(DrugOrdering, site=esr21_pharmacy_admin)
class DrugOrderingAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugOrderingForm

    fieldsets = (
        (None, {
            'fields': (
                'next_ap_date',
                'current_inventory',
                'study_product_name',
                'drug_code',
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
                    'received_intact',
                    'status_comment',
                    'departure_temp',
                    'arrival_temp',
                    'temp_control_during_trans',
                    'transportation_control_comment'
                )
            })
        ),
        audit_fieldset_tuple
    )
