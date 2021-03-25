from rich import print

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from lib.version import get_joomla_version_1

connection_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'
}

def connection_check(args):
    try:
        response = requests.get(args.u, verify=False, timeout=10, allow_redirects=False, headers=connection_headers)
        status_code = response.status_code

        if(status_code == 200):
            print(f'[green][INF] Connected successfully with {args.u} | {status_code} [/]')
            joomla_check_1(args)
        else:
            return print(f'[red][ERR] Connection problems with {args.u} | {status_code} [/]')

    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e} [/]')

    except requests.exceptions.MissingSchema:
        return print(f'[red][ERR] Invalid URL, please use http or https before the URL.')


def joomla_check_1(args):
    admin_path = f"{args.u}/administrator"
    admin_text = "Joomla!"

    try:
        admin_request = requests.get(admin_path, verify=False, timeout=10, allow_redirects=True, headers=connection_headers)
        body = admin_request.text
        status_code = admin_request.status_code

        if(status_code == 200 and admin_text in body):
            print('[green][INF] Joomla detected successfully on first check. [/]')
            get_joomla_version_1(args)
        else:
            print(f"\n[yellow][WRN] Can't find Joomla admin login, passing check... [/]")
            joomla_check_2(args)

    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')


def joomla_check_2(args):
    joomla_logo_path = f"{args.u}/administrator/templates/khepri/images/h_green/j_header_left.png"

    try:
        logo_request = requests.get(joomla_logo_path, verify=False, timeout=10, allow_redirects=False, headers=connection_headers)
        status_code = logo_request.status_code

        if(status_code == 200):
            print('[green][INF] Joomla detected successfully on second check. [/]')
            get_joomla_version_1(args)
        else:
            print(f"[yellow][WRN] Can't find Joomla logo, passing check... [/]")
            joomla_check_3(args)

    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')


def joomla_check_3(args):
    joomla_robots = f"{args.u}/robots.txt"

    try:
        robots_request = requests.get(joomla_robots, verify=False, timeout=10, allow_redirects=False, headers=connection_headers)
        status_code = robots_request.status_code
        body = robots_request.text
        
        if(status_code == 200 and 'Joomla' or '/components' in body):
            print('[green][INF] Joomla detected successfully on third check. [/]')
            get_joomla_version_1(args)
        else:
            print(f"[yellow][WRN] Can't find Joomla logo, passing check... [/]")
            joomla_check_4(args)
    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')


def joomla_check_4(args):
    manifest_path = f'{args.u}/administrator/manifests/files/joomla.xml'
    language_path = f'{args.u}/language/en-GB/en-GB.xml'

    try:
        manifest_request = requests.get(manifest_path, verify=False, timeout=10, allow_redirects=False, headers=connection_headers)
        language_request = requests.get(language_path, verify=False, timeout=10, allow_redirects=False, headers=connection_headers)

        status_code = manifest_request.status_code
        status_code_2 = language_request.status_code

        if(status_code or status_code_2 == 200):
            print('\n[green][INF] 50% chance that Joomla has been detected... [/]')
            get_joomla_version_1(args)
        else:
            return print(f'[red][ERR] Joomla has not found, stopping... [/]')  

    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')   