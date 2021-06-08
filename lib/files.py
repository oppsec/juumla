from rich import print

from requests import get, exceptions

from urllib3 import disable_warnings
disable_warnings()

from lib.manager import props
from lib.info import config_files_scan


files = ['configuration.php~','configuration.php.new','configuration.php.new~','configuration.php.old','configuration.php.old~','configuration.bak','configuration.php.bak','configuration.php.bkp','configuration.txt','configuration.php.txt','configuration - Copy.php','configuration.php.swo','configuration.php_bak','configuration.orig','configuration.php.save','configuration.php.original','configuration.php.swp','configuration.save','.configuration.php.swp','configuration.php1','configuration.php2','configuration.php3','configuration.php4','configuration.php4','configuration.php6','configuration.php7','configuration.phtml','configuration.php-dist']


def files_finder(args: str) -> str:

    print(config_files_scan)

    for file in files:
        url = f"{args.u}/{file}"

        try:
            response = get(url, **props)
            status_code = response.status_code

            if(status_code == 200):
                print(f"[green][INF] Possible readable config file found: {url} [/]")
            else:
                continue
            
        except exceptions.ConnectionError as e:
            return print(f'\n[red][ERR] Connection problems with {url} | {e} [/]')