from despatchbay.despatchbay_sdk import DespatchBaySDK

client = DespatchBaySDK(api_user='<APIUSER>', api_key='<APIKEY')

tracking = client.get_tracking('DEMO1234567890123456')
print(tracking)
