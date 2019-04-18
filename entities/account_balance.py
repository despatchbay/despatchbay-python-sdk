class AccountBalance(object):
    def __init__(self, client, balance=None, available=None):
        self.account_client = client.account_client
        self.type_name = 'ns1:BalanceType'
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

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.account_client.factory.create(self.type_name)
        suds_object.Balance = self.balance
        suds_object.AvailableBalance = self.available
        return suds_object
