from entities import courier


class Service(object):
    def __init__(self, client, service_id, service_format, name, cost, courier):
        self.client = client
        self.type_name = 'ns1:ServiceType'
        self.service_id = service_id
        self.format = service_format
        self.name = name
        self.cost = cost
        self.courier = courier

    @classmethod
    def from_dict(cls, client, soap_dict):
        """
        Alternative constructor, builds entity object from a dictionary representation of
        a SOAP response created by the SOAP client.
        """
        return cls(
            client=client,
            service_id=soap_dict.get('ServiceID', None),
            service_format=soap_dict.get('Format', None),
            name=soap_dict.get('Name', None),
            cost=soap_dict.get('Cost', None),
            courier=courier.Courier.from_dict(
                client,
                client.shipping_client.dict(soap_dict.get('Courier', None))
            )
        )

    def to_soap_object(self):
        """
        Creates a SOAP client object representation of this entity.
        """
        suds_object = self.client.factory.shipping_client.create(self.type_name)
        suds_object.CourierID = self.service_id
        suds_object.CourierName = self.name
        return suds_object
