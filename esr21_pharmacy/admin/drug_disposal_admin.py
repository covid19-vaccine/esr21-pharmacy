from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin

from ..admin import ModelAdminMixin
from ..models.drug_disposal import DrugDisposal
from ..models.drug_disposal import Signatures
from ..forms.drug_disposal_forms import DrugDisposalForm
from ..forms.drug_disposal_forms import SignaturesForm
from ..admin_site import esr21_pharmacy_admin


class SignatureInLineAdmin(TabularInlineMixin, admin.TabularInline):
    model = Signatures
    form = SignaturesForm
    extra = 1

    fieldsets = (
        ('Dose spillage documentation', {
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
