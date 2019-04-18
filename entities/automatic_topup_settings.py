class AutomaticTopupSettings(object):
    def __init__(self, client, minimum_balance=None, topup_amount=None, payment_method_id=None):
        self.client = client
        self.type_name = 'ns1:AutomaticTopupsSettingsRequestType'
        self.minimum_balance = minimum_balance
        self.topup_amount = topup_amount
        self.payment_method_id = payment_method_id

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            minimum_balance=soap_dict.get('MinimumBalance', None),
            topup_amount=soap_dict.get('TopupAmount', None),
            payment_method_id=soap_dict.get('PaymentMethodID', None)
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.client.account_client.factory.create(self.type_name)
        suds_object.MinimumBalance = self.minimum_balance
        suds_object.TopupAmount = self.topup_amount
        suds_object.PaymentMethodID = self.payment_method_id
        return suds_object
