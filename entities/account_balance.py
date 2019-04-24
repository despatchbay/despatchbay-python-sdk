from entities.entity import Entity


class AccountBalance(Entity):
    SOAP_MAP = {
        'Balance': {
            'property': 'balance',
            'type': 'float'
        },
        'AvailableBalance': {
            'property': 'available',
            'type': 'float'
        }
    }

    SOAP_TYPE = 'ns1:AccountBalanceType'

    def __init__(self, client, balance=None, available=None):
        super().__init__(self.SOAP_TYPE, client.account_client, self.SOAP_MAP)
        self.balance = balance
        self.available = available

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            balance=soap_dict.get('Balance', None),
            available=soap_dict.get('AvailableBalance', None)
        )
