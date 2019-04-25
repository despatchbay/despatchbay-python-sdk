from despatchbay.despatchbay_sdk import DespatchBaySDK
import pprint

client = DespatchBaySDK(api_user='2MTN-C5I9R355', api_key='114LS25D', api_domain='api.despatchbay.st')
# client = DespatchBaySDK(api_user='D2N3C-7DB9EC51', api_key='676BE721E048AFA69151')
account_return = client.get_account()
print(account_return.__dict__)
print(account_return.to_soap_object())

services_return = client.get_services()
for returned_service in services_return:
    print(returned_service.__dict__)

print('='*20)
account_balance = client.get_account_balance()
print(account_balance.balance)
print(account_balance.available)

print('='*20)
sender_addresses = client.get_sender_addresses()
print(sender_addresses[0].__dict__)
print(sender_addresses[0].sender_address.__dict__)

print('='*20)
payment_methods = client.get_payment_methods()
for payment_method in payment_methods:
    pprint.pprint(payment_method.__dict__)
    print(payment_method.to_soap_object())

print('='*20)
print('Automatic topup enabled?', client.enable_automatic_topups('100', payment_methods[0].payment_method_id, payment_methods[0].payment_method_id))


print('='*20)
print('Automatic topups disabled?', client.disable_automatic_topups())
