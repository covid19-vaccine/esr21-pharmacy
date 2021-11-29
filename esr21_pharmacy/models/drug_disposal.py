from django.db import models
from django.db.models import PROTECT
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
