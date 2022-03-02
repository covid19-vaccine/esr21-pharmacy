from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, audit_fields

from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import esr21_pharmacy_admin
from ..forms.drug_requisition_form import DrugRequisitionForm
from ..models.drug_requisition import DrugRequisition


@admin.register(DrugRequisition, site=esr21_pharmacy_admin)
class DrugRequisitionAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugRequisitionForm

    fieldsets = (
        (None, {
            'fields': (
                'tracking_identifier',
                'injection_site',
                'date',
                'quantity_order',
            )
        }),
        audit_fieldset_tuple
    )

    search_fields = ('tracking_identifier',)

    radio_fields = {'injection_site': admin.VERTICAL}

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj) + audit_fields +
                ('tracking_identifier',))
