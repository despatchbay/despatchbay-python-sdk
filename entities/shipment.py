class Shipment(object):
    def __init__(self, client, service_id=None, parcels=None, client_reference=None, collection_date=None, sender_address=None, recipient_address=None, follow_shipment=None):
        self.client = client
        self.type_name = 'ns1:ShipmentRequestType'
        self.service_id = service_id
        self.parcels = parcels
        self.client_reference = client_reference
        self.collection_date = collection_date
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.follow_shipment = follow_shipment

    def to_soap_object(self):
        suds_object = self.client.factory.create(self.type_name)
        parcel_array = self.client.factory.create('ns1:ArrayOfParcelType')
        soap_parcel_list = []
        for item in self.parcels:
            soap_parcel_list.append(item.to_soap_object())
        print(soap_parcel_list)
        parcel_array.item = soap_parcel_list
        parcel_array._arrayType = "urn:ParcelType[]"
        collection_date = self.client.factory.create('CollectionDateType')
        collection_date.CollectionDate = self.collection_date
        suds_object.ServiceID = self.service_id
        suds_object.Parcels = parcel_array
        suds_object.ClientReference = self.client_reference
        suds_object.CollectionDate = collection_date
        suds_object.SenderAddress = self.sender_address.to_soap_object()
        suds_object.RecipientAddress = self.recipient_address.to_soap_object()
        suds_object.FollowShipment = self.follow_shipment
        return suds_object
