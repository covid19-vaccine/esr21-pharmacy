from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin

from ..models.drug_notification import DrugNotification
from ..forms.drug_notification_form import DrugNotificationForm
from ..admin_site import esr21_pharmacy_admin


@admin.register(DrugNotification, site=esr21_pharmacy_admin)
class DrugNotificationAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = DrugNotificationForm

    filter_horizontal = ('reasons_for_treatment_discontinuation',)

    fieldsets = (
        (None, {
            'fields': (
                'pid',
                'participant_initials',
                'date_of_discontinuation',
                'reasons_for_treatment_discontinuation',
                'completed_by',
            )
        }), audit_fieldset_tuple
    )
