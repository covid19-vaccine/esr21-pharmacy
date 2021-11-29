from django.db import models
from django.db.models import PROTECT
from edc_base.model_mixins import BaseUuidModel


class DrugAccountabilityLog(BaseUuidModel):
    site = models.CharField(
        verbose_name='Injection site name',
        max_length=25,
    )

    study_name = models.CharField(
        verbose_name='Study name',
        default='AZD1222-ESR-21-21311',
        max_length=20
    )

    investigator = models.CharField(
        verbose_name='Investigator of Record Name',
        default='Dr Joseph Makhema',
        max_length=20
    )

    study_product_name = models.CharField(
        verbose_name='Study Product Name',
        max_length=100,
        default='AstraZeneca Covid-19 vaccine',
    )

    manufacturer = models.CharField(
        verbose_name='Manufacturer',
        max_length=100,
        default='AstraZeneca',
    )

    storage_temp = models.CharField(
        verbose_name='Storage temperature',
        max_length=100,
        default='2-8 °C',
    )

    package_size = models.CharField(
        verbose_name='Package size',
        default='5ml vials',
        max_length=25
    )

    lot_number = models.CharField(
        verbose_name='Lot number',
        max_length=20
    )

    exp_date = models.DateTimeField(
        verbose_name='Expiration Date',
    )


class DrugAccountabilityLogInline(BaseUuidModel):
    drug = models.ForeignKey(DrugAccountabilityLog, on_delete=PROTECT)

    date = models.DateTimeField(
        verbose_name='Date',
    )

    requisition_form_number = models.CharField(
        verbose_name='Requisition form number',
        max_length=25
    )

    details = models.CharField(
        verbose_name='Details',
        max_length=100

    )

    received_or_issued = models.IntegerField(
        verbose_name='Quantity received or issues'
    )

    balance_forward = models.IntegerField(
        verbose_name='Balance forward'
    )

    status = models.IntegerField(
        verbose_name='Status (Active/Quarantined/Disposed)'
    )

    comments = models.TextField(
        verbose_name='Comment'
    )

    registered_pharmacist_initials = models.CharField(
        verbose_name='R.Ph. Initials',
        max_length=5

    )

    qc_initial = models.CharField(
        verbose_name='QC initial',
        max_length=3
    )

    qc_initial_date = models.DateField(
        verbose_name='QC initial date'
    )
