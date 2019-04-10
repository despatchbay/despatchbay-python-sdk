import account_balance


class Account(object):
    arg_map = {
        'AccountID': 'id',
        'AccountName': 'name',
        'AccountBalance': 'balance'
    }

    def __init__(self, client, id=None, name=None, balance=None):
        self.client = client
        self.type_name = 'ns1:AccountType'
        self.id = id
        self.name = name
        self.balance = balance

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            id=kwargs.get('AccountID', None),
            name=kwargs.get('AccountName', None),
            balance=account_balance.AccountBalance.from_dict(
                client,
                **client.accounts_client.dict(kwargs.get('AccountBalance', None))
            )
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.AccountID = self.id
        suds_object.AccountName = self.name
        suds_object.AccountBalance = self.balance
        return suds_object
