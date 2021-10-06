from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from .modeladmin_mixins import ModelAdminMixin

from ..models.drug_accountability_log import DrugAccountabilityLogInline
from ..models.drug_accountability_log import DrugAccountabilityLog
from ..forms.drug_accountability_log_form import DrugAccountabilityLogInLineForm
from ..forms.drug_accountability_log_form import DrugAccountabilityLogForm
from ..admin_site import esr21_pharmacy_admin


class DrugAccountabilityLogInLineAdmin(TabularInlineMixin, admin.StackedInline):
    model = DrugAccountabilityLogInline
    form = DrugAccountabilityLogInLineForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': (
                'date',
                'requisition_form_number',
                'details',
                'received_or_issued',
                'balance_forward',
                'status',

            )
        }
         ),
        ('', {
            'fields': (
                'comments',
                'registered_pharmacist_initials',
                'qc_initial',
                'qc_initial_date',
            )
        }
         ),
    )


@admin.register(DrugAccountabilityLog, site=esr21_pharmacy_admin)
class DrugAccountabilityLogAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugAccountabilityLogForm

    inlines = [DrugAccountabilityLogInLineAdmin, ]

    readonly_fields = (
        'study_name', 'investigator', 'study_product_name', 'manufacturer', 'storage_temp', 'package_size')

    fieldsets = (
        (None, {
            'fields': (
                'site',
                'study_name',
                'investigator',
                'study_product_name',
                'manufacturer',
                'storage_temp',
                'package_size',
                'lot_number',
                'exp_date',
            )
        }
         ),
    )
