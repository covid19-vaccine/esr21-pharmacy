from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin

from ..admin import ModelAdminMixin
from ..admin_site import esr21_pharmacy_admin
from ..models.drug_dose_administration import DrugDoseAdministration
from ..forms.drug_dose_administration_form import DrugDoseAdministrationForm
from ..forms.drug_dose_administration_form import DosageSpillageForm
from ..models.drug_dose_administration import DosageSpillage


class DosageSpillageInlineAdmin(TabularInlineMixin, admin.TabularInline):
    model = DosageSpillage
    form = DosageSpillageForm
    extra = 1

    fieldsets = (
        ('Dose spillage documentation', {
            'fields': (
                'is_there_spillage',
                'volume_spilled',
                'administered_by'
            )
        }
         ),
    )


@admin.register(DrugDoseAdministration, site=esr21_pharmacy_admin)
class DrugDoseAdministrationAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugDoseAdministrationForm

    inlines = [DosageSpillageInlineAdmin, ]

    fieldsets = (
        (None, {
            'fields': (
                'participant_initials',
                'pid',
                'date_of_consent',
                'details',
            )
        }),
        ('Dose One', {
            'fields': (
                'batch_number_dose_one',
                'expiration_date_dose_one',
                'date_injection_dose_one',
            )
        }),
        ('Dose Two', {
            'fields': (
                'batch_number_dose_two',
                'expiration_date_dose_two',
                'date_injection_dose_two',
            )
        }),
        audit_fieldset_tuple
    )
