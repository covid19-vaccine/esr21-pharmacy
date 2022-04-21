from edc_form_validators import FormValidator


class DrugAccountabilityLogFormValidator(FormValidator):
    def clean(self):
        site = self.cleaned_data.get('injection_site')
        self.required_if_true(condition=site is 'CMS',
                              field='injection_site',
                              field_required='quantity_received')

        not_req_fields = ['quantity_order', 'issued']

        for filed in not_req_fields:
            self.not_applicable_if('CMS',
                                   field='injection_site',
                                   field_applicable=filed)
