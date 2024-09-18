import requests

def get_latest_rate(from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    inverse_rate = 1 / rate
    return rate, inverse_rate

def get_historical_rate(from_currency, to_currency, date):
    url = f"https://api.frankfurter.app/{date}?from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    inverse_rate = 1 / rate
    return rate, inverse_rate
