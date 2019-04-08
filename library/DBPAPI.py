from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds import WebFault, TypeNotFound
from entities import parcel, address, recipient, sender, shipment


class DespatchBayAPI(object):

    def __init__(self, apiuser, apikey):
        # todo: set differently
        url = 'http://api.despatchbay.st/soap/%s/%s?wsdl'
        account_url = url  % ('v14', 'account')
        shipping_url = url  % ('v15', 'shipping')
        t1 = HttpAuthenticated(username=apiuser, password=apikey)
        t2 = HttpAuthenticated(username=apiuser, password=apikey)
        t3 = HttpAuthenticated(username=apiuser, password=apikey)
        t4 = HttpAuthenticated(username=apiuser, password=apikey)
        self.accounts_client = Client(account_url,  transport=t1)
        self.addressing_client = Client(shipping_url,  transport=t2)
        self.shipping_client = Client(shipping_url,  transport=t3)
        self.tracking_client = Client(shipping_url,  transport=t4)

    # Shipping entities

    def parcel(self, **kwargs):
        """
        Creates a dbp parcel entity
        """
        return parcel.Parcel(self.shipping_client, **kwargs)

    def address(self, **kwargs):
        """
        Creates a dbp address entity
        """
        return address.Address(self.shipping_client, **kwargs)

    def recipient(self, **kwargs):
        """
        Creates a dbp recipient address entity
        """
        return recipient.Recipient(self.shipping_client, **kwargs)

    def sender(self, **kwargs):
        """
        Creates a dbp sender address entity
        """
        return sender.Sender(self.shipping_client, **kwargs)

    def shipment(self, **kwargs):
        """
        Creates a dbp shipment entity
        """
        return shipment.Shipment(self.shipping_client, **kwargs)

    # Account Services

    def get_account(self):
        return self.accounts_client.service.GetAccount()

    def get_account_balance(self):
        return self.accounts_client.service.GetAccountBalance()

    def get_sender_addresses(self):
        return self.accounts_client.service.GetSenderAddresses()

    # Shipping services

    def get_available_services(self, shipment_request):
        return self.shipping_client.service.GetAvailableServices(
            shipment_request.to_soap_object())

    def get_collection(self, collection_id):
        return self.shipping_client.service.GetCollection(collection_id)

    def get_collections(self):
        return self.shipping_client.service.GetCollections()

    def get_available_collection_dates(self, sender_address, courier_id):
        try:
            return self.shipping_client.service.GetAvailableCollectionDates(
                sender_address.to_soap_object(), courier_id)
        except TypeNotFound as e:
            print("last sent: ")
            print(self.shipping_client.last_sent())

    def get_shipment(self, shipment_id):
        return self.shipping_client.service.GetShipment(shipment_id)

    def add_shipment(self, shipment_request):
        return self.shipping_client.service.AddShipment(shipment_request.to_soap_object())

    def book_shipments(self, shipment_ids):
        return self.shipping_client.service.BookShipments(shipment_ids)

    def cancel_shipment(self, shipment_id):
        return self.shipping_client.service.CancelShipment(shipment_id)
