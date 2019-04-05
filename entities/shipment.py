from entity import Entity


class Shipment(Entity):
    def __init__(self, client, service_id=None, parcels=None, client_reference=None, collection_date=None, sender_address=None, recipient_address=None, follow_shipment=None):

        Entity.__init__(self, client)

        self.type_name = 'ns1:ShipmentRequestType'
        self.suds_object = self.client.factory.create(self.type_name)
        self.suds_object.ServiceID = service_id

        parcel_array = client.factory.create('ns1:ArrayOfParcelType')
        parcel_list = []
        for item in parcels:
            parcel_list.append(item.get_soap_object())
        parcel_array.item = parcel_list
        parcel_array._arrayType = "SOMETHING"

        self.suds_object.Parcels = parcel_array
        self.suds_object.ClientReference = client_reference
        self.suds_object.CollectionDate = collection_date
        self.suds_object.SenderAddress = sender_address.get_soap_object()
        self.suds_object.RecipientAddress = recipient_address.get_soap_object()
        self.suds_object.FollowShipment = follow_shipment


    def get_soap_object(self):
        return self.suds_object





