from entities.entity import Entity


class AutomaticTopupSettings(Entity):
    SOAP_MAP = {
        "MinimumBalance": {
            "property": "minimum_balance",
            "type": "float"
        },
        "TopupAmount": {
            "property": "topup_amount",
            "type": "float"
        },
        "PaymentMethodID": {
            "property": "payment_method_id",
            "type": "string"
        }
    }
    SOAP_TYPE = 'ns1:AutomaticTopupsSettingsRequestType'

    def __init__(self, client, minimum_balance=None, topup_amount=None, payment_method_id=None):
        super().__init__(self.SOAP_TYPE, client.account_client, self.SOAP_MAP)
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
