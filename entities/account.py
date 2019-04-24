from entities import account_balance
from entities.entity import Entity


class Account(Entity):

    # todo: entity class
    SOAP_MAP = {
        'AccountID': {
            'property': 'account_id',
            'type': 'integer'
        },
        'AccountName': {
            'property': 'name',
            'type': 'string'
        },
        'AccountBalance': {
            'property': 'balance',
            'type': 'entity',
            # 'entityClass': 'DespatchBay\Entity\AccountBalance'
        }
    }

    SOAP_TYPE = 'ns1:AccountType'

    def __init__(self, client, account_id=None, name=None, balance=None):
        super().__init__(self.SOAP_TYPE, client.account_client, self.SOAP_MAP)
        self.account_id = account_id
        self.name = name
        self.balance = balance

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            account_id=soap_dict.get('AccountID', None),
            name=soap_dict.get('AccountName', None),
            balance=account_balance.AccountBalance.from_dict(
                client,
                client.account_client.dict(soap_dict.get('AccountBalance', None))
            )
        )
