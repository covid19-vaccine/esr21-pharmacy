from django.db import models
from edc_base import get_utcnow
from edc_base.model_mixins import BaseUuidModel


class DrugAccountabilityLog(BaseUuidModel):
    site = models.CharField(
        verbose_name='Injection site name',
        max_length=25,
        blank=True,
    )

    lot_number = models.CharField(
        verbose_name='Lot number',
        max_length=20,

    )

    exp_date = models.DateTimeField(
        verbose_name='Expiration Date',
        default=""
    )

    date = models.DateTimeField(
        verbose_name='Date',
        default=get_utcnow
    )

    requisition_form_number = models.CharField(
        verbose_name='Requisition form number',
        max_length=25,
        null=True,
        blank=True
    )

    details = models.TextField(
        verbose_name='Details',
        null=True,
        blank=True

    )

    received_or_issued = models.IntegerField(
        verbose_name='Quantity received or issues',
        null=True,
        blank=True
    )

    balance_forward = models.IntegerField(
        verbose_name='Balance forward',
        null=True,
        blank=True
    )

    status = models.IntegerField(
        verbose_name='Status (Active/Quarantined/Disposed)',
        null=True,
        blank=True
    )

    comments = models.TextField(
        verbose_name='Comment',
        null=True,
        blank=True
    )

    class Meta:
        app_label = 'esr21_pharmacy'
        verbose_name = 'Drug Accountability'
        verbose_name_plural = 'Drug Accountability'
