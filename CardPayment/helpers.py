import json
import requests

# Helper methods

# Get authorization token using API key
def get_auth_token(api_key):
    url = 'https://accept.paymob.com/api/auth/tokens'
    params = {
        "api_key": api_key
    }
    response = requests.post(url=url, json=params)
    return response.json()

# Register an order
def register_order(auth_token, delivery_needed, amount_cents, items):
    url = 'https://accept.paymob.com/api/ecommerce/orders'
    params = {
        'auth_token': auth_token,
        'delivery_needed': delivery_needed,
        'amount_cents': amount_cents,
        'items': items
    }
    response = requests.post(url=url, json=params)
    return response.json()

# Request Payment key
def request_payment_key(auth_token, amount_cents, expiration, order_id, currency, integration_id):
    url = 'https://accept.paymob.com/api/acceptance/payment_keys'
    params = {
        'auth_token': auth_token,
        'amount_cents': amount_cents,
        'expiration': expiration,
        'order_id': order_id,
        'billing_data': {
            "apartment": "NA", 
            "email": "claudette09@exa.com", 
            "floor": "NA", 
            "first_name": "Clifford", 
            "street": "Ethan Land", 
            "building": "NA", 
            "phone_number": "+86(8)9135210487", 
            "shipping_method": "NA", 
            "postal_code": "NA", 
            "city": "NA", 
            "country": "NA", 
            "last_name": "Nicolas", 
            "state": "NA"
        },
        'currency': currency,
        'integration_id': integration_id
    }
    response = requests.post(url=url, json=params)
    return response.json()