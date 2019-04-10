import courier


class Service(object):
    def __init__(self,client, id, service_format, name, cost, courier):
        self.client = client
        self.type_name = 'ns1:CourierType'
        self.id = id
        self.format = service_format
        self.name = name
        self.cost = cost
        self.courier = courier

    @classmethod
    def from_dict(cls, client, **kwargs):
        return cls(
            client=client,
            id=kwargs.get('ServiceID', None),
            service_format=kwargs.get('Format', None),
            name=kwargs.get('Name', None),
            cost=kwargs.get('Cost', None),
            courier=courier.Courier.from_dict(
                client,
                **client.dict(kwargs.get('Courier', None))
            )
        )

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        suds_object.CourierID= self.id
        suds_object.CourierName = self.name
        return suds_object
