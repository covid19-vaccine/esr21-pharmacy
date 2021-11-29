from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO


class DrugRequisition(BaseUuidModel):

    injection_site = models.CharField(
        verbose_name='Injection site name',
        max_length=25,
    )

    investigator = models.CharField(
        verbose_name='Investigator of Record Name',
        default='Dr Joseph Makhema',
        max_length=20
    )

    date = models.DateField(
        verbose_name='Date',
    )

    inventory = models.IntegerField(
        verbose_name='Current Inventory',
    )

    study_product_name = models.CharField(
        verbose_name='Study Product Name',
        max_length=100,
        default='AstraZeneca Covid-19 vaccine',
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

    acceptable_temp_range = models.CharField(
        verbose_name='Acceptable temperature range for study product',
        default='2 to 8 °C',
        max_length=10
    )

    delivery_site_temp = models.IntegerField(
        verbose_name='Cooler-box temperature reading at delivery to site',
        help_text='°C'
    )

    last_dose_temp = models.IntegerField(
        verbose_name='Cooler-box temperature reading when last dose was given',
        help_text='°C'
    )

    temp_control_during_trans = models.CharField(
        verbose_name='Was the temperature control acceptable during use at injection site?',
        choices=YES_NO,
        max_length=10
    )

    transportation_control_comment = models.TextField(
        verbose_name='Comment',
    )
