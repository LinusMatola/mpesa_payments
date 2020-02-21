import requests
import base64
from requests.auth import HTTPBasicAuth

from datetime import datetime
import keys


unformated_time = datetime.now()
formated_time = unformated_time.strftime("%Y%m%d%H%M%S")



data_to_encode = keys.businessShortCode + keys.lipa_na_mpesa_passkey + formated_time

encoded_string = base64.b64encode(data_to_encode.encode())

decoded_password = encoded_string.decode('utf-8')


consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    
json_response = (r.json())

generated_access_token = json_response['access_token']

def lipa_na_mpesa():
 
        access_token = generated_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        request = {
                "BusinessShortCode": keys.businessShortCode,
                "Password": decoded_password,
                "Timestamp": formated_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": "1",
                "PartyA": keys.phone_number,
                "PartyB": keys.businessShortCode,
                "PhoneNumber": keys.phone_number,
                "CallBackURL": "https://xxxxxxxxxxx.com/callback",
                "AccountReference": "xxxxxx",
                "TransactionDesc": "Payment to matlynventures"
        }
        
        response = requests.post(api_url, json = request, headers=headers)
        
        print (response.text)

lipa_na_mpesa()