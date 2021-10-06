from edc_constants.constants import OTHER
from edc_list_data import PreloadData

list_data = {
    'esr21_pharmacy.neighborhoodproblems': [
        ('HIV / AIDS', 'HIV / AIDS'),
        ('Schools', 'Schools'),
        ('Sewer', 'Sewer'),
        ('Unemployment', 'Unemployment'),
        ('Roads', 'Roads'),
        ('Water', 'Water'),
        ('House', 'House'),
        ('Malaria', 'Malaria'),
        (OTHER, 'Other (specify)'),
    ],
    'esr21_pharmacy.discontinuation': [
        ('Completed both doses', 'Completed both doses'),
        ('complications during administration(life threatening reactions)', 'complications during administration'),
        ('de-consented before completion of doses', 'de-consented before completion of doses'),
    ]
}

preload_data = PreloadData(
    list_data=list_data)
