class PaymentMethod(object):
    def __init__(self, client, payment_method_id=None, payment_method_type=None, description=None):
        self.client = client
        self.type_name = 'ns1:PaymentMethod'
        self.payment_method_id = payment_method_id
        self.type = payment_method_type
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

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.client.shipping_client.factory.create(self.type_name)
        suds_object.PaymentMethodID = self.payment_method_id
        suds_object.Type = self.type
        suds_object.Description = self.description
        return suds_object
