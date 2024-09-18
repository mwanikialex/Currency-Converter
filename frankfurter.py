import requests

def get_currencies():
    url = "https://api.frankfurter.app/currencies"
    response = requests.get(url)
    data = response.json()
    currencies = list(data.keys())
    return currencies
