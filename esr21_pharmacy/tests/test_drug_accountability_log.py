from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from ..form_validations.drug_accountability_log_form_validator import \
    DrugAccountabilityLogFormValidator


@tag('drug')
class TestDrugAccountabilityLog(TestCase):

    def test_cms_drug_update(self):
        """
        Raise Error if CMS data is captured incorrectly
        """
        clean_data = {
            'injection_site': 'CMS',
            'quantity_received': 21,
            'quantity_order': 111,
            'issued': 21
        }
        form_validator = DrugAccountabilityLogFormValidator(cleaned_data=clean_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('quantity_order', form_validator._errors)
        self.assertIn('issued', form_validator._errors)
        self.assertNotIn('quantity_received', form_validator._errors)
