from despatchbay.despatchbay_sdk import DespatchBaySDK

client = DespatchBaySDK(api_user='<APIUSER>', api_key='<APIKEY>')

account_return = client.get_account()
print(account_return)

services_return = client.get_services()
print(services_return)

account_balance = client.get_account_balance()
print(account_balance)

sender_addresses = client.get_sender_addresses()
print(sender_addresses)

payment_methods = client.get_payment_methods()
print(payment_methods)

automatic_topup_enabled = client.enable_automatic_topups(
    '100', payment_methods[0].payment_method_id, payment_methods[0].payment_method_id)
print(automatic_topup_enabled)

automatic_topup_disabled = client.disable_automatic_topups()
print(automatic_topup_disabled)
