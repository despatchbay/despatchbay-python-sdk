from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.plugin import MessagePlugin
from suds import WebFault
import suds
from entities import parcel, address, recipient, sender, shipment

class dbpapi(object):

    def __init__(self):
        # todo: set differently
        url = 'http://api.despatchbay.com/soap/%s/%s?wsdl'
        account_url = url  % ('v14', 'account')
        shipping_url = url  % ('v14', 'shipping')

        # todo: don't hardcode auth
        auth = ['user', 'pass']
        t1 = HttpAuthenticated(username=auth[0], password=auth[1])
        t2 = HttpAuthenticated(username=auth[0], password=auth[1])
        t3 = HttpAuthenticated(username=auth[0], password=auth[1])
        t4 = HttpAuthenticated(username=auth[0], password=auth[1])
        self.accounts_client = Client(account_url,  transport=t1)
        self.addressing_client = Client(shipping_url,  transport=t2)
        self.shipping_client = Client(shipping_url,  transport=t3)
        self.shipping_client.
        self.tracking_client = Client(shipping_url,  transport=t4)

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

    def get_available_services(self, shipment_request):
        try:
            return self.shipping_client.service.GetAvailableServices(shipment_request)
        except WebFault as e:
            print("error!")
            print(e)
            print(self.shipping_client.last_sent())

    def add_shipment(self, shipment_request):
        return self.shipping_client.service.AddShipment(shipment_request)
