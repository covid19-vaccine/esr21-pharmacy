from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class RequisitionIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'requisition_identifier'
    template = '{device_id}{random_string}'
    make_human_readable = True
