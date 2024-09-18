def format_conversion_result(rate, inverse_rate, amount, from_currency, to_currency, date):
    converted_amount = amount * rate
    result = (f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate:.5f}. "
              f"So {amount} in {from_currency} corresponds to {converted_amount:.2f} in {to_currency}. "
              f"The inverse rate was {inverse_rate:.5f}.")
    return result
