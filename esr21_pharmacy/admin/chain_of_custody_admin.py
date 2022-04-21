from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from ..admin_site import esr21_pharmacy_admin
from ..forms import ChainOfCustodyUploadForm
from ..models import ChainOfCustodyUpload


@admin.register(ChainOfCustodyUpload, site=esr21_pharmacy_admin)
class ChainOfCustodyUploadAdmin(TabularInlineMixin, admin.ModelAdmin):
    form = ChainOfCustodyUploadForm

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
