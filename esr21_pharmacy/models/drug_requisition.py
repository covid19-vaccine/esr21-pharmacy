from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager, SiteModelMixin


class DrugRequisition(BaseUuidModel, SiteModelMixin):
    injection_site = models.CharField(
        verbose_name='Injection site name',
        max_length=25,
    )

    date = models.DateField(
        verbose_name='Date',
    )

    quantity_order = models.IntegerField(
        verbose_name='Quantity Order'
    )

    quantity_issued = models.IntegerField(
        verbose_name='Quantity issued'
    )

    batch_number = models.CharField(
        verbose_name='Batch Number',
        max_length=25,
    )

    exp_date = models.DateTimeField(
        verbose_name='Expiration Date',
    )

    quantity_received = models.IntegerField(
        verbose_name='Quantity received'
    )

    on_site = CurrentSiteManager()


    class Meta:
        app_label = 'esr21_pharmacy'
        verbose_name = 'Drug Requisition'
        verbose_name_plural = 'Drug Requisition'
