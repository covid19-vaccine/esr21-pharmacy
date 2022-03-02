from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import esr21_pharmacy_admin
from ..forms.drug_disposal_forms import DrugDisposalForm, DrugDisposalUploadForm
from ..forms.drug_disposal_forms import SignaturesForm
from ..models.drug_disposal import DrugDisposal, DrugDisposalUpload
from ..models.drug_disposal import Signatures


class SignatureInLineAdmin(TabularInlineMixin, admin.TabularInline):
    model = Signatures
    form = SignaturesForm
    extra = 1

    fieldsets = (
        ('Drug Disposable receivers', {
            'fields': (
                'print_name',
                'designation',
                'initials',
                'date',
            )
        }
         ),
    )


@admin.register(DrugDisposal, site=esr21_pharmacy_admin)
class DrugDisposalAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugDisposalForm

    inlines = [SignatureInLineAdmin]

    fieldsets = (
        ('Dose spillage documentation', {
            'fields': (
                'date',
                'study_product_name',
                'product_dosage_form',
                'lot_number',
                'quantity',
                'reasons',
                'pharmacist_initials',
            )
        }
         ),
    )


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
