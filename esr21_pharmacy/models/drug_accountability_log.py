from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db import models
from edc_base import get_utcnow
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin

from esr21_pharmacy.choices import site_names, statuses


class DrugAccountabilityLog(SiteModelMixin, BaseUuidModel):
    injection_site = models.CharField(
        verbose_name='Site name',
        max_length=25,
        blank=True,
        choices=site_names,

    )

    lot_number = models.CharField(
        verbose_name='Lot number',
        max_length=20,
        default=None
    )

    exp_date = models.DateTimeField(
        verbose_name='Expiration Date',
        validators=[
            MinValueValidator(limit_value=timezone.now())
        ]
    )

    date = models.DateTimeField(
        verbose_name='Date',
        default=get_utcnow
    )

    tracking_identifier = models.CharField(
        verbose_name='Requisition form number',
        max_length=25,
        null=True,
        blank=True
    )

    details = models.TextField(
        verbose_name='Details',
        default="VAC008001"
    )

    issued = models.IntegerField(
        verbose_name='Quantity issued',
        null=True,
        blank=True
    )

    quantity_order = models.IntegerField(
        verbose_name='Quantity ordered',
        null=True,
        blank=True
    )
    quantity_received = models.IntegerField(
        verbose_name='Quantity received',
        null=True,
        blank=True
    )

    balance = models.IntegerField(
        verbose_name='Balance Forward',
        null=True,
        blank=True
    )

    status = models.CharField(
        verbose_name='Status',
        null=True,
        max_length=30,
        choices=statuses
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
