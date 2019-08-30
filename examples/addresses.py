from despatchbay.despatchbay_sdk import DespatchBaySDK

client = DespatchBaySDK(api_user='<APIUSER>', api_key='<APIKEY>')

address_1 = client.find_address('DN227AY', '1')
print(address_1)

address_2 = client.get_address_by_key('DN227AY0001')
print(address_2)

address_3 = client.get_address_keys_by_postcode('DN22 7AY')
print(address_3)
