from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from ..admin_site import esr21_pharmacy_admin
from ..forms.drug_disposal_forms import DrugDisposalUploadForm
from ..models.drug_disposal import DrugDisposalUpload


@admin.register(DrugDisposalUpload, site=esr21_pharmacy_admin)
class DrugDisposalUploadAdmin(TabularInlineMixin, admin.ModelAdmin):
    form = DrugDisposalUploadForm

    fieldsets = (
        (None, {
            'fields': (
                'description',
                'document',
                'user_uploaded',
                'datetime_captured',
            )
        }
         ),
    )
