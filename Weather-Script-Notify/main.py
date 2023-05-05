# import requests
# from twilio.rest import Client
#
# account_sid = "ACea7c68a0cc414f111be0d69cd8ce0cb1"
# auth_token = "a3fbbde36f31f2a9b35fae8f23a8b03b"
# api_website = "https://api.openweathermap.org/data/2.5/forecast"
# api_key = "98f47a4903b0269d6a5d49877feae015"
#
# website_parameter = {
#     "lat": 28.682280,
#     "lon": 77.023700,
#     "appid": api_key,
# }
# response = requests.get(api_website, params=website_parameter)
# data = response.json()
# data_slice = data["list"][:6]
#
# is_rain = False
#
# for item in data_slice:
#     item_id = item["weather"][0]["id"]
#     if item_id < 700:
#         is_rain = True
#
# if is_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body="Hello from Twilio",
#         from_="+16205018161",
#         to="+917827353115"
#     )
#
import requests
import os
from twilio.rest import Client

account_sid = "ACea7c68a0cc414f111be0d69cd8ce0cb1"
auth_token = os.environ.get("owm_auth_key")
api_website = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("api_key")

website_parameter = {
    "lat": 28.682280,
    "lon": 77.023700,
    "appid": api_key,
}
response = requests.get(api_website, params=website_parameter)
print(response.status_code)
data = response.json()
data_slice = data["list"][:6]

is_rain=False

for item in data_slice:
    item_id = item["weather"][0]["id"]
    if item_id < 700:
        is_rain = True

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="This is made for test of rain project check if today is rain or not at morning and if rain then send message by twillo the code is running on pythonanywhere",
        from_="+16205018161",
        to="+917827353115"
    )


