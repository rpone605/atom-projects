import requests
import socket
import ssl

HOST = "https://unemploymen-ohio-gov.com/loginc.php"
PORT = 443

url = 'https://unemploymen-ohio-gov.com/loginc.php'

data = {
    'USR_LOGIN_NAME': '',
    'USR_LTPD_PASSWORD': '',
}

response = requests.post(url, data=data).text
