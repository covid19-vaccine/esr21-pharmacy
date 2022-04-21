from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from ..admin_site import esr21_pharmacy_admin
from ..forms import IncidentReportUploadForm
from ..models import IncidentReportUpload


@admin.register(IncidentReportUpload, site=esr21_pharmacy_admin)
class IncidentReportUploadAdmin(TabularInlineMixin, admin.ModelAdmin):
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
