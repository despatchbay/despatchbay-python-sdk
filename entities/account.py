import account_balance


class Account(object):
    def __init__(self, client, account_id=None, name=None, balance=None):
        self.account_client = client.account_client
        self.type_name = 'ns1:AccountType'
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

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.account_client.factory.create(self.type_name)
        suds_object.AccountID = self.account_id
        suds_object.AccountName = self.name
        suds_object.AccountBalance = self.balance
        return suds_object
