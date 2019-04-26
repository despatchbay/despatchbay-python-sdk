


# normal
client = despatchbay_sdk.DespatchBaySDK(api_user='2MTN-C5I9R355', api_key='114LS25D', api_domain='api.despatchbay.st')
#demo
# self.client = DBPAPI.DespatchBayAPI(apiuser='2MTN-3C7B9E45', apikey='7E33ABC14613E3251846')

my_parcel_1 = client.parcel(weight=1, length=1, width=1, height=1, contents=1, value=1, tracking_number=None)
print(my_parcel_1.__dict__)
print(my_parcel_1.to_soap_object())
my_parcel_2 = client.parcel(weight=30, length=99, width=99, height=99, contents='balloons', value=1)
print(my_parcel_2.__dict__)
print(my_parcel_2.to_soap_object())
my_address = client.address(
    company_name="Acme",
    country_code="GB",
    county="",
    locality="",
    postal_code="sw1a1aa",
    town_city="London",
    street="Buckingham Palace"
)
print(my_address.__dict__)
print(my_address.to_soap_object())
recipient = client.recipient(name="scott", telephone="foo", email="bar", recipient_address=my_address)
sender = client.sender(name="Al", telephone="foo", email="bar", sender_address=my_address)
shipment_request = client.shipment_request(parcels=[my_parcel_1, my_parcel_2], client_reference='puchacz',
                                                collection_date='2019-04-10', sender_address=sender,
                                                recipient_address=recipient, follow_shipment='true')
print(shipment_request.to_soap_object())
services = client.get_available_services(shipment_request)
for service in services:
    print(service.courier.to_soap_object())
shipment_request.service_id = services[0].service_id
dates = client.get_available_collection_dates(sender, services[0].courier.courier_id)
print(dates)
shipment_request.collection_date = dates[0]
print(shipment_request.__dict__)
print(shipment_request.collection_date.__dict__)
# print('+++++++++++++++++++++')
# print(shipment_request.collection_date.to_soap_object())
# print('+++++++++++++++++++++')
# added_shipment = client.add_shipment(shipment_request)
# client.book_shipments([added_shipment])
# shipment_return = client.get_shipment(added_shipment)
# label_pdf = client.fetch_shipment_labels(shipment_return.shipment_document_id)
# label_pdf.download('./new_pdf.pdf')
