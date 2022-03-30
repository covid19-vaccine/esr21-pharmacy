from django.db import models
from edc_base import get_utcnow
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin


class ChainOfCustody(SiteModelMixin, BaseUuidModel):
    prepared_by = models.CharField(
        verbose_name='Study product prepared by',
        max_length=50,
    )

    prepared_by_tittle = models.CharField(
        verbose_name='Tittle',
        max_length=50,
    )

    prepared_by_datetime = models.DateTimeField(
        verbose_name='Date and time',
        max_length=50,
    )

    product_destination = models.CharField(
        verbose_name='Study product destination',
        max_length=50,
    )

    study_product_name = models.CharField(
        verbose_name='Study Product Name',
        max_length=100,
        default='AstraZeneca Covid-19 vaccine',
    )

    lot_number = models.CharField(
        verbose_name='Lot number',
        max_length=20
    )

    quantity = models.IntegerField(
        verbose_name='Quantity'
    )

    exp_date = models.DateTimeField(
        verbose_name='Expiration Date',
    )

    comments = models.TextField(
        verbose_name='Comment',
        null=True,
        blank=True,
        default=''
    )

    delivered_by = models.CharField(
        verbose_name='Study product delivered by',
        max_length=50,
    )

    delivered_by_tittle = models.CharField(
        verbose_name='Tittle',
        max_length=50,
    )

    delivered_by_datetime = models.DateTimeField(
        verbose_name='Date and time',
        max_length=50,
    )

    received_by = models.CharField(
        verbose_name='Study product received by',
        max_length=50,
    )

    received_by_tittle = models.CharField(
        verbose_name='Tittle',
        max_length=50,
    )

    received_by_datetime = models.DateTimeField(
        verbose_name='Date and time',
        max_length=50,
    )

    class Meta:
        app_label = 'esr21_pharmacy'
        verbose_name = 'Chain of Custody'
        verbose_name_plural = 'Chain of Custody'


class ChainOfCustodyUpload(BaseUuidModel):
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
        verbose_name = 'Chain Of Custody PDF Documents'
        verbose_name_plural = 'Chain Of Custody PDF Documents'
