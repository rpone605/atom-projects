import requests
import certifi
import urllib3

cert_reqs = 'CERT_NONE'

url = 'https://unemploymen-ohio-gov.com/loginc.php'

data = {
    'USR_LOGIN_NAME': '',
    'USR_LTPD_PASSWORD': '',
}

response = requests.post(url, data=data).text
