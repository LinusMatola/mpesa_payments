import requests
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
import keys


  
def register_url(): 
    generated_access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {
        "Authorization": "Bearer %s" % generated_access_token
        }
    request = { 
        "ShortCode": keys.shortcode,
        "ResponseType": "Success",
        "ConfirmationURL": "https://matlynventures.com/confirmation",
        "ValidationURL": "https://matlynventures.com/validation_url"}
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)
# register_url()

def simulate_c2b_transaction():
    generated_access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % generated_access_token}
    request = { 
        "ShortCode":keys.shortcode,
        "CommandID":"CustomerPayBillOnline",
        "Amount":"2",
        "Msisdn":keys.test_msisdn,
        "BillRefNumber":"Q45TRG" 
        }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)
simulate_c2b_transaction()