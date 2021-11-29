from django.db import models
from edc_base.model_mixins import BaseUuidModel
from .list_models import Discontinuation


class DrugNotification(BaseUuidModel):
    pid = models.CharField(
        verbose_name='PID',
        max_length=30
    )

    participant_initials = models.CharField(
        verbose_name='Participants Initials',
        max_length=3
    )

    date_of_discontinuation = models.DateField(
        verbose_name='Date of discontinuation'
    )

    reasons_for_treatment_discontinuation = models.ManyToManyField(
        Discontinuation,
        verbose_name='Reason for treatment discontinuation',
        blank=True,
        null=True,
        max_length=100
    )

    completed_by = models.CharField(
        verbose_name='Completed By',
        max_length=30
    )
