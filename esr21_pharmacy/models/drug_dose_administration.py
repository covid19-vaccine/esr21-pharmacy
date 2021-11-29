from django.db import models
from django.db.models import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO


class DrugDoseAdministration(BaseUuidModel):
    participant_initials = models.CharField(
        verbose_name='participant Initials',
        max_length=3
    )

    pid = models.CharField(
        verbose_name='PID',
        max_length=25
    )

    date_of_consent = models.DateField(
        verbose_name='Date of consent',
        help_text='for ENTRY/ RECONSENT only',
    )

    details = models.CharField(
        verbose_name='Details',
        default='AZD1222 Covid-19 vaccine 0.5ml',
        help_text='Route of Administration: (IM)Injection',
        max_length=30
    )

    batch_number_dose_one = models.CharField(
        verbose_name='Batch Number',
        max_length=20
    )

    expiration_date_dose_one = models.DateField(
        verbose_name='Expiration Date',
    )

    date_injection_dose_one = models.DateField(
        verbose_name='Date of Injection',
    )

    batch_number_dose_two = models.CharField(
        verbose_name='Batch Number',
        max_length=20
    )

    expiration_date_dose_two = models.DateField(
        verbose_name='Expiration Date',
    )

    date_injection_dose_two = models.DateField(
        verbose_name='Date of Injection',
    )


class DosageSpillage(BaseUuidModel):
    drug = models.ForeignKey(DrugDoseAdministration, on_delete=PROTECT)

    is_there_spillage = models.CharField(
        verbose_name='Was there a spillage that required re-drawing',
        max_length=5,
        choices=YES_NO
    )

    volume_spilled = models.IntegerField(
        verbose_name='Indicate the volume of the spill',
        help_text='ml',
    )

    administered_by = models.CharField(
        verbose_name='Administered by',
        max_length=40
    )

    history = HistoricalRecords()
