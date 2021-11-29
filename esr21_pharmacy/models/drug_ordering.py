from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO


class DrugOrdering(BaseUuidModel):
    next_ap_date = models.DateField(
        verbose_name='Date',
    )

    current_inventory = models.IntegerField(
        verbose_name='Current Inventory',
    )

    study_product_name = models.CharField(
        verbose_name='Study Product Name',
        max_length=100,
        default='AstraZeneca Covid-19 vaccine',
    )

    drug_code = models.CharField(
        verbose_name='Drug Code',
        max_length=50,
    )

    units = models.CharField(
        verbose_name='Units',
        default='5ml vials',
        max_length=25
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

    study_product_ordered_by = models.CharField(
        verbose_name='Study product ordered by',
        max_length=50,
    )

    title = models.CharField(
        verbose_name='Tittle',
        max_length=50,
    )

    ordered_by_date_time = models.DateTimeField(
        verbose_name='Date',
    )

    received_intact = models.CharField(
        verbose_name='Was study product received intact?',
        choices=YES_NO,
        max_length=10
    )

    status_comment = models.TextField(
        verbose_name='Comment',
    )

    departure_temp = models.IntegerField(
        verbose_name='Departure cooler-box temperature reading',
        help_text='°C'
    )

    arrival_temp = models.IntegerField(
        verbose_name='Arrival cooler-box temperature reading',
        help_text='°C'
    )

    temp_control_during_trans = models.CharField(
        verbose_name='Was the temperature control acceptable during transport?',
        choices=YES_NO,
        max_length=10
    )

    transportation_control_comment = models.TextField(
        verbose_name='Comment',
    )
