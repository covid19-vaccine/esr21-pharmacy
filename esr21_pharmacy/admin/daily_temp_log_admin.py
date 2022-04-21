from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from ..admin_site import esr21_pharmacy_admin
from ..forms import DailTempLogUploadForm
from ..models import DailyTempLogUpload


@admin.register(DailyTempLogUpload, site=esr21_pharmacy_admin)
class DailTempLogUploadAdmin(TabularInlineMixin, admin.ModelAdmin):
    form = DailTempLogUploadForm

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
