from rich import print
from requests import get, exceptions

from src.juumla.settings import props

def files_manager(args) -> None:
    """ Search for sensitive readable files on target """

    print("\n[cyan][INF] Searching for sensitive readable files [/]")

    files = ['configuration.php~','configuration.php.new','configuration.php.new~','configuration.php.old','configuration.php.old~','configuration.bak','configuration.php.bak','configuration.php.bkp','configuration.txt','configuration.php.txt','configuration - Copy.php','configuration.php.swo','configuration.php_bak','configuration.orig','configuration.php.save','configuration.php.original','configuration.php.swp','configuration.save','.configuration.php.swp','configuration.php1','configuration.php2','configuration.php3','configuration.php4','configuration.php4','configuration.php6','configuration.php7','configuration.phtml','configuration.php-dist']

    for file in files:
        url = f"{args.u}/{file}"

        try:
            response = get(url, **props)
            status_code = response.status_code

            if(status_code == 200):
                print(f"[green][INF] Possible readable config file found: {url} [/]")
            else:
                pass
            
        except exceptions.ConnectionError as e:
            return print(f'\n[red][ERR] Connection problems with {url} | {e} [/]')

    print("[yellow][WRN] Finished Joomla sensitive readable files scanner... [/]")