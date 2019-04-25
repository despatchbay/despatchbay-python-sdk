from entity import Entity


class PaymentMethod(Entity):

    SOAP_MAP = {
        'PaymentMethodID': {
            'property': 'payment_method_id',
            'type': 'integer'
        },
        'Type': {
            'property': 'payment_method_type',
            'type': 'string'
        },
        'Description': {
            'property': 'description',
            'type': 'string'
        }
    }
    SOAP_TYPE = 'ns1:PaymentMethodType'

    def __init__(self, client, payment_method_id=None, payment_method_type=None, description=None):
        super().__init__(self.SOAP_TYPE, client.account_client, self.SOAP_MAP)
        self.payment_method_id = payment_method_id
        self.payment_method_type = payment_method_type
        self.description = description

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            payment_method_id=soap_dict.get('PaymentMethodID', None),
            payment_method_type=soap_dict.get('Type', None),
            description=soap_dict.get('Description', None)
        )
