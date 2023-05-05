import requests
import itertools

from twilio.rest import Client

currency_url = "https://www.alphavantage.co/query"
news_url = "https://www.alphavantage.co/query"
stock_api_key = "EB05XC682T1N04DX"

account_sid = "ACea7c68a0cc414f111be0d69cd8ce0cb1"
auth_token = "a3fbbde36f31f2a9b35fae8f23a8b03b"


def create_msg(n_d_s):
    msg = ""
    for nds in n_d_s:
        news_titile = nds["title"]
        news_summary = nds["summary"]
        news_source = nds["source"]
        msg = msg + f'{news_titile}\n{news_summary}\n{news_source}\n\n'
    return msg


currency_parameter = {
    "function": "FX_DAILY",
    "from_symbol": "USD",
    "to_symbol": "INR",
    "apikey": stock_api_key,
}
news_parameter = {
    "function": "NEWS_SENTIMENT",
    "tickers": "FOREX:INR",
    "apikey": stock_api_key,
}
response = requests.get(url=currency_url, params=currency_parameter)
response.raise_for_status()
stock_data = response.json()

stock_data_two_days = dict(itertools.islice(stock_data["Time Series FX (Daily)"].items(), 2))
difference = 0
for items in stock_data_two_days.values():
    difference = abs(difference-float(items["4. close"]))

if round(difference, 2) >= 1:
    news_response = requests.get(url=news_url, params=news_parameter)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_data_slice = news_data["feed"][:5]
    get_msg = create_msg(news_data_slice)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{get_msg}",
        from_="+16205018161",
        to="+917827353115"
    )



