from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager, SiteModelMixin
from edc_identifier.model_mixins import TrackingIdentifierModelMixin

from ..choices import site_names
from ..identifiers import RequisitionIdentifier


class DrugRequisition(TrackingIdentifierModelMixin, BaseUuidModel,
                      SiteModelMixin):

    tracking_identifier_cls = RequisitionIdentifier

    tracking_identifier = models.CharField(
        verbose_name="Requisition Form Number",
        max_length=36,
        unique=True,
        editable=False
    )

    injection_site = models.CharField(
        verbose_name='Injection site name',
        max_length=25,
        choices=site_names,
    )

    date = models.DateTimeField(
        verbose_name='Date',
    )

    quantity_order = models.IntegerField(
        verbose_name='Quantity Order'
    )

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    def __str__(self):
        return f'{self.tracking_identifier}, {self.tracking_identifier}'

    def natural_key(self):
        return self.tracking_identifier

    def save(self, *args, **kwargs):
        if not self.tracking_identifier:
            self.tracking_identifier = self.tracking_identifier_cls().identifier
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'esr21_pharmacy'
        verbose_name = 'Drug Requisition'
        verbose_name_plural = 'Drug Requisition'
