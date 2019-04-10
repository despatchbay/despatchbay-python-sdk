class AccountBalance(object):
    arg_map = {
        'Balance': 'balance',
        'AvailableBalance': 'available'
    }

    def __init__(self, client, balance=None, available=None):
        self.client = client
        self.type_name = 'ns1:BalanceType'
        self.balance = balance
        self.available = available

    @classmethod
    def from_dict(cls, client, **kwargs):
        print(kwargs)
        return cls(
            client=client,
            balance=kwargs.get('Balance', None),
            available=kwargs.get('AvailableBalance', None)
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.Balance= self.balance
        suds_object.AvailableBalance = self.available
        return suds_object
