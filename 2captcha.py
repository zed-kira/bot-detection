import requests
import time


def bypass_captcha():
    
    API_KEY = '<YOUR-API-KEY-HERE>'
    data_sitekey = '<CAPTCHA-DATA-SITEKEY-HERE'
    page_url ='<the website url where your captcha appears>'
    request_url = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"

    response = requests.get(request_url).json()
    print(response)

    rid = response.get("request")
    token_url = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"

    form_token = ""

    while True:
        token_response = requests.get(token_url).json()
        print(token_response)

        if token_response.get("status") == 1:
            # get the solution : a token that we need to update our browser with.
            form_token = token_response.get("request")
            break
        time.sleep(1)


    return form_token