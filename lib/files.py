from rich import print

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import os

files = ['configuration.php~','configuration.php.new','configuration.php.new~','configuration.php.old','configuration.php.old~','configuration.bak','configuration.php.bak','configuration.php.bkp','configuration.txt','configuration.php.txt','configuration - Copy.php','configuration.php.swo','configuration.php_bak','configuration.php#','configuration.orig','configuration.php.save','configuration.php.original','configuration.php.swp','configuration.save','.configuration.php.swp','configuration.php1','configuration.php2','configuration.php3','configuration.php4','configuration.php4','configuration.php6','configuration.php7','configuration.phtml','configuration.php-dist']
connection_headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'}

def files_finder(args):
    print('[cyan][INF] Trying to find config files... [/]')
    for file in files:
        url = f"{args.u}/{file}"

        try:
            response = requests.get(url, verify=False, allow_redirects=False, headers=connection_headers)
            status_code = response.status_code

            if(status_code == 200):
                print(f"[green][INF] Found possible config file: {url}")
            else:
                pass
            
        except requests.exceptions.ConnectionError as e:
            return print(f'\n[red][ERR] Connection problems with {url} | {e}[/]')