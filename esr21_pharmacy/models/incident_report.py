from django.db import models
from edc_base import get_utcnow
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin


class IncidentReport(SiteModelMixin, BaseUuidModel):
    study_site = models.CharField(
        verbose_name='Study site',
        max_length=50,
    )

    report_date = models.DateField(
        verbose_name='Date',
        max_length=50,
    )

    incident_description = models.TextField(
        verbose_name='Description of the incident',
    )

    witness = models.CharField(
        verbose_name='Witnessed or Incident report verified by',
        max_length=50,
    )

    reporter = models.CharField(
        verbose_name='reported by',
        max_length=50,
    )

    reporter_sign = models.CharField(
        verbose_name='Sign',
        max_length=50,
    )

    witness_sign = models.CharField(
        verbose_name='Witnessed or Incident report verified by(Name and Signature)',
        max_length=50,
        help_text='Another person at the study site have to counter sign for the incident'
    )

    received_by = models.CharField(
        verbose_name='Report received by',
        max_length=50,
    )

    received_by_sign = models.CharField(
        verbose_name='Sign',
        max_length=50,
    )

    received_date = models.DateField(
        verbose_name='Received date'
    )

    class Meta:
        app_label = 'esr21_pharmacy'
        verbose_name = 'Drug Incident and Temperature Excursion Report'
        verbose_name_plural = 'Drug Incident and Temperature Excursion Report'


class IncidentReportUpload(BaseUuidModel):
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
        verbose_name = 'Incident Report PDF Documents'
        verbose_name_plural = 'Incident Report PDF Documents'
