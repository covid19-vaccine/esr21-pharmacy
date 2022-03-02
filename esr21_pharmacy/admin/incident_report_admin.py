from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin

from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import esr21_pharmacy_admin
from ..forms import IncidentReportForm, IncidentReportUploadForm
from ..models import IncidentReport, IncidentReportUpload


@admin.register(IncidentReport, site=esr21_pharmacy_admin)
class IncidentReportAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = IncidentReportForm

    fieldsets = (
        (None, {
            'fields': (
                'study_site',
                'report_date',
                'incident_description',
                'witness',
                'reporter',
                'reporter_sign',
                'witness_sign',
                'received_by',
                'received_by_sign',
                'received_date',
            )
        }),
        audit_fieldset_tuple
    )

@admin.register(IncidentReportUpload, site=esr21_pharmacy_admin)
class DrugDisposalUploadAdmin(TabularInlineMixin, admin.ModelAdmin):
    form = IncidentReportUploadForm

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
