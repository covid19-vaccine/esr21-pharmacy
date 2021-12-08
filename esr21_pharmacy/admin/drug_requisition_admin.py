from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin

from ..models.drug_requisition import DrugRequisition
from ..forms.drug_requisition_form import DrugRequisitionForm
from ..admin_site import esr21_pharmacy_admin


@admin.register(DrugRequisition, site=esr21_pharmacy_admin)
class DrugRequisitionAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugRequisitionForm

    fieldsets = (
        (None, {
            'fields': (
                'injection_site',
                'date',
                'quantity_order',
                'quantity_issued',
                'batch_number',
                'exp_date',
                'quantity_received',
            )
        }),
        audit_fieldset_tuple
    )
