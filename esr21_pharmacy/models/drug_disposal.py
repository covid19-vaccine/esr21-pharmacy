from django.db import models
from django.db.models import PROTECT
from edc_base import get_utcnow
from edc_base.model_mixins import BaseUuidModel

from ..choices import designations


class DrugDisposal(BaseUuidModel):
    date = models.DateField(
        verbose_name='date'
    )

    study_product_name = models.CharField(
        verbose_name='Study Product Name',
        max_length=100,
        default='AstraZeneca Covid-19 vaccine',
    )

    product_dosage_form = models.CharField(
        verbose_name='Units',
        default='5ml vials',
        max_length=25
    )

    lot_number = models.CharField(
        verbose_name='Lot number',
        max_length=20
    )

    quantity = models.IntegerField(
        verbose_name='Quantity'
    )

    reasons = models.TextField(
        verbose_name='Reasons for return and disposal'
    )

    pharmacist_initials = models.CharField(
        verbose_name='Pharmacist\'s Initials',
        max_length=5
    )


class Signatures(BaseUuidModel):
    notification = models.ForeignKey(
        DrugDisposal,
        on_delete=PROTECT
    )

    print_name = models.CharField(
        verbose_name='Print_name',
        max_length=50
    )

    designation = models.CharField(
        choices=designations,
        verbose_name='Designation',
        max_length=50
    )

    initials = models.CharField(
        verbose_name='Initials',
        max_length=5
    )

    date = models.DateField(
        verbose_name='Date'
    )

    class Meta:
        app_label = 'esr21_pharmacy'
        verbose_name = 'Drug Disposal'
        verbose_name_plural = 'Drug Disposal'


class DrugDisposalUpload(BaseUuidModel):

    description = models.CharField(
        verbose_name='Description',
        max_length=255,
        blank=True
    )

    document = models.FileField(upload_to='document/')

    user_uploaded = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='user uploaded', )

    datetime_captured = models.DateTimeField(
        default=get_utcnow)

    class Meta:
        app_label = 'esr21_pharmacy'
        verbose_name = 'Drug Disposal PDF Documents'
        verbose_name_plural = 'Drug Disposal PDF Documents'
