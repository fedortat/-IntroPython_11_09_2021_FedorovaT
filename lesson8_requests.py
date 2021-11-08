import requests
from requests_oauthlib import OAuth1
import os

KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")

auth = OAuth1(KEY, SECRET)
endpoint = f"http://api.thenounproject.com/icon/{id}"

response = requests.get(endpoint, auth=auth)
res = response.json()

icon_url = res["icon"]["icon_url"]

icon_res = requests.get(icon_url)
icon = icon_res.content

save_dir = "icons"
os.makedirs(save_dir, exist_ok=True)

filename = "1.svg"

with open(os.path.join(save_dir, filename), "bw") as file:  # запись в байтах
    file.write(icon)


##################################################################
# def get_raw_quote(key):
#     url = "http://api.forismatic.com/api/1.0/"
#     params = {"method": "getQuote",
#               "format": "json",
#               "key": key,
#               "lang": "en"}
#
#     r = requests.get(url, params=params)
#     try:
#         quote = r.json()
#     except Exception:
#         quote = {}
#     return quote
#
# for key in range(10):
#     quote = get_raw_quote(key)
#     print(quote)
