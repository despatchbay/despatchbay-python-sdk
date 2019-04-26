import despatchbay_sdk

client = despatchbay_sdk.DespatchBaySDK(api_user='2MTN-C5I9R355', api_key='114LS25D', api_domain='api.despatchbay.st')
# client = despatchbay_sdk.DespatchBaySDK(api_user='D2N3C-7DB9EC51', api_key='676BE721E048AFA69151')
print(client.addressing_client)

address = client.find_address('ln69zd', '17')
print(address.__dict__)
print(address.to_soap_object())

address = client.get_address_by_key('wd65jb1015')
print(address.__dict__)
print(address.to_soap_object())

for address in client.get_address_keys_by_postcode('wd6 5jb'):
    print(address.__dict__)
    print(address.to_soap_object())
