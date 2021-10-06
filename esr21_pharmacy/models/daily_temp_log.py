from django.db import models
from edc_base.model_mixins import BaseUuidModel


class DailyTempLog(BaseUuidModel):
    site = models.CharField(
        verbose_name='Injection site name',
        max_length=25,
    )

    date = models.DateTimeField(
        verbose_name='Date and Time'
    )

    investigator = models.CharField(
        verbose_name='Investigator of record name',
        default='Dr Joseph Makhema',
        max_length=30
    )

    product_name = models.CharField(
        verbose_name='Study product name',
        default='AstraZeneca Vaccine AZD1222',
        max_length=30
    )

    current_temp = models.IntegerField(
        verbose_name='Current',
        help_text='°C',
    )

    initials = models.CharField(
        verbose_name='Name/Initials',
        max_length=20
    )

    comments = models.TextField(
        verbose_name='Comments'
    )
