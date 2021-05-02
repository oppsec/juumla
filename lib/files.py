from rich import print

import requests
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from lib.agent import get_user_agent

headers = {'User-Agent': get_user_agent()}

files = ['configuration.php~','configuration.php.new','configuration.php.new~','configuration.php.old','configuration.php.old~','configuration.bak','configuration.php.bak','configuration.php.bkp','configuration.txt','configuration.php.txt','configuration - Copy.php','configuration.php.swo','configuration.php_bak','configuration.php','configuration.orig','configuration.php.save','configuration.php.original','configuration.php.swp','configuration.save','.configuration.php.swp','configuration.php1','configuration.php2','configuration.php3','configuration.php4','configuration.php4','configuration.php6','configuration.php7','configuration.phtml','configuration.php-dist']

def files_finder(args):
    print('[cyan][INF] Trying to find config files... [/]')
    for file in files:
        url = f"{args.u}/{file}"

        try:
            response = requests.get(url, verify=False, allow_redirects=False, headers=headers)
            status_code = response.status_code

            if(status_code == 200):
                print(f"[green][INF] Possible readable config file found: {url}")
            else:
                pass
            
        except requests.exceptions.ConnectionError as e:
            return print(f'\n[red][ERR] Connection problems with {url} | {e}[/]')