from despatchbay.despatchbay_sdk import DespatchBaySDK

client = DespatchBaySDK(api_user='<APIUSER>', api_key='<APIKEY>')

my_parcel_1 = client.parcel(
    weight=3,
    length=14,
    width=15,
    height=92,
    contents='Apples',
    value=65
)
my_parcel_2 = client.parcel(
    weight=30,
    length=100,
    width=100,
    height=100,
    contents='Oranges',
    value=1
)
recipient_address = client.address(
    company_name="Acme",
    country_code="GB",
    county="Theshire",
    locality="Placeton",
    postal_code="ps76de",
    town_city="Cityville",
    street="123 Fake Street"
)

recipient = client.recipient(
    name="Bonnie Bobbins",
    telephone="01632987654",
    email="bonnie@example.com",
    recipient_address=recipient_address

)
# Sender using address_id
sender = client.sender(
    name="Joe Bloggs",
    telephone="01632123456",
    email="acme@example.com",
    address_id='123456'
)

shipment_request = client.shipment_request(
    parcels=[my_parcel_1, my_parcel_2],
    client_reference='puchacz',
    collection_date='2019-04-01',
    sender_address=sender,
    recipient_address=recipient,
    follow_shipment='true'
)

services = client.get_available_services(shipment_request)
shipment_request.service_id = services[0].service_id
dates = client.get_available_collection_dates(sender, services[0].courier.courier_id)
shipment_request.collection_date = dates[0]
added_shipment = client.add_shipment(shipment_request)
client.book_shipments([added_shipment])
shipment_return = client.get_shipment(added_shipment)
label_pdf = client.get_labels(shipment_return.shipment_document_id)
label_pdf.download('./new_label.pdf')
