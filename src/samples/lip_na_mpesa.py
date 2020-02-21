import requests
from encode import generate_password
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
import keys
from utils import get_timestamp


def lipa_na_mpesa():
        formated_time = get_timestamp()
        decoded_password = generate_password(formated_time)
        access_token = generate_access_token()

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
                "CallBackURL": "https://matlynventures.com/callback",
                "AccountReference": keys.phone_number,
                "TransactionDesc": "Payment to matlynventures"
        }
        
        response = requests.post(api_url, json = request, headers=headers)
        
        print (response.text)

lipa_na_mpesa()