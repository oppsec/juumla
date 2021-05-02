from rich import print

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from lib.version import get_joomla_version
from lib.agent import get_user_agent

headers = {'User-Agent': get_user_agent()}

def connection_check(args):
    try:
        response = requests.get(args.u, verify=False, timeout=10, allow_redirects=False, headers=headers)
        status_code = response.status_code

        if(status_code == 200):
            print(f'[green][INF] Connected successfully with {args.u} | {status_code} [/]')
            first_check(args)
        else:
            return print(f'[red][ERR] Connection problems with {args.u} | {status_code} [/]')

    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e} [/]')

    except requests.exceptions.MissingSchema:
        return print(f'[red][ERR] Invalid URL, please use http or https before the URL.')


def first_check(args):
    print('\n[cyan][INF] Trying to detect Joomla... [/]')
    admin_path = f"{args.u}/administrator"
    admin_text = "Joomla!"

    try:
        admin_request = requests.get(admin_path, verify=False, timeout=10, allow_redirects=True, headers=headers)
        body = admin_request.text
        status_code = admin_request.status_code

        if(status_code == 200 and admin_text in body):
            print('[green][INF] Joomla detected successfully on 1° check. [/]')
            get_joomla_version(args)
        else:
            print(f"[yellow][WRN] Can't detect Joomla admin login, passing check... (1° check)  [/]")
            second_check(args)

    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')


def second_check(args):
    joomla_logo_path = f"{args.u}/administrator/templates/khepri/images/h_green/j_header_left.png"

    try:
        logo_request = requests.get(joomla_logo_path, verify=False, timeout=10, allow_redirects=False, headers=headers)
        status_code = logo_request.status_code

        if(status_code == 200):
            print('[green][INF] Joomla detected successfully on 2° check. [/]')
            get_joomla_version(args)
        else:
            print(f"[yellow][WRN] Can't detect Joomla logo, passing check... (2° check) [/]")
            third_check(args)

    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')


def third_check(args):
    joomla_robots = f"{args.u}/robots.txt"

    try:
        robots_request = requests.get(joomla_robots, verify=False, timeout=10, allow_redirects=False, headers=headers)
        status_code = robots_request.status_code
        body = robots_request.text
        
        if(status_code == 200 and 'Joomla' or '/components' in body):
            print('[green][INF] Joomla detected successfully on 3° check. [/]')
            get_joomla_version(args)
        else:
            print(f"[yellow][WRN] Can't detect Joomla on body, passing check... (3° check) [/]")
            fourth_check(args)
    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')


def fourth_check(args):
    try:
        response = requests.get(args.u, verify=False, timeout=10, allow_reditects=False, headers=headers)
        status_code = response.status_code
        body = response.text

        if(status_code == 200 and '<meta name="generator" content="Joomla' in body):
            print('[green][INF] Joomla detected successfully on 4° check. [/]')
            get_joomla_version(args)
        else:
            print(f"[yellow][WRN] Can't detect Joomla meta generator tag, passing check... (4° check) [/]")
            fifth_check(args)
            
    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')


def fifth_check(args):
    try:
        response = requests.get(args.u, verify=False, timeout=10, allow_reditects=False, headers=headers)
        status_code = response.status_code
        body = response.text

        if(status_code == 200 and '/index.php?option=com_search' in body):
            print('[green][INF] Joomla detected successfully on 5° check. [/]')
            get_joomla_version(args)
        else:
            print(f"[yellow][WRN] Can't detect Joomla search method, passing check... (5° check) [/]")
            last_check(args)
            
    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')


def last_check(args):
    manifest_path = f'{args.u}/administrator/manifests/files/joomla.xml'
    language_path = f'{args.u}/language/en-GB/en-GB.xml'

    try:
        manifest_request = requests.get(manifest_path, verify=False, timeout=10, allow_redirects=False, headers=headers)
        language_request = requests.get(language_path, verify=False, timeout=10, allow_redirects=False, headers=headers)

        manifest_status_code = manifest_request.status_code
        language_status_code = language_request.status_code

        if(manifest_status_code or language_status_code == 200):
            print('\n[green][INF] 50% chance that Joomla has been detected... [/]')
            get_joomla_version(args)
        else:
            return print(f'[red][ERR] Joomla has not found, stopping... [/]')  

    except requests.exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e}[/]')   