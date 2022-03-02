from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin

from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import esr21_pharmacy_admin
from ..forms import ChainOfCustodyForm, ChainOfCustodyUploadForm
from ..models import ChainOfCustody, ChainOfCustodyUpload


@admin.register(ChainOfCustody, site=esr21_pharmacy_admin)
class ChainOfCustodyAmin(ModelAdminMixin, admin.ModelAdmin):
    form = ChainOfCustodyForm

    fieldsets = (
        (None, {
            'fields': (
                'prepared_by',
                'prepared_by_tittle',
                'prepared_by_datetime',
            )
        }),
        ('Product Details', {
            'fields': (
                'product_destination',
                'study_product_name',
                'lot_number',
                'quantity',
                'exp_date',
                'comments',

            )
        }),
        ('Delivered By', {
            'fields': (
                'delivered_by',
                'delivered_by_tittle',
                'delivered_by_datetime',
            )
        }),
        ('Received By', {
            'fields': (
                'received_by',
                'received_by_tittle',
                'received_by_datetime',
            )
        }),
        audit_fieldset_tuple
    )


@admin.register(ChainOfCustodyUpload, site=esr21_pharmacy_admin)
class DrugDisposalUploadAdmin(TabularInlineMixin, admin.ModelAdmin):
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
