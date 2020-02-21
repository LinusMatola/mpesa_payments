import base64
import keys

def generate_password(formated_time):

    data_to_encode = keys.businessShortCode + keys.lipa_na_mpesa_passkey + formated_time

    encoded_string = base64.b64encode(data_to_encode.encode())

    decoded_password = encoded_string.decode('utf-8')
    
    return decoded_password