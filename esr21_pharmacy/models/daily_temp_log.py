from django.db import models
from edc_base import get_utcnow
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin


class DailyTempLogUpload(SiteModelMixin, BaseUuidModel):
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
        verbose_name = 'Upload Daily Temperature Log PDF Document'
        verbose_name_plural = 'Daily Temperature Log PDF Documents'
