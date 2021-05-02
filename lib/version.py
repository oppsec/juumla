from rich import print

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from lib.files import files_finder
from lib.agent import get_user_agent

import os
import xmltodict

first_xml_header = 'application/xml'
second_xml_header = 'text/xml'

headers = {'User-Agent': get_user_agent()}


def get_joomla_version(args):
    print('\n[cyan][INF] Trying to get Joomla version... [/]')

    manifest_path = f'{args.u}/administrator/manifests/files/joomla.xml'

    try:
        response = requests.get(manifest_path, verify=False, timeout=10, allow_redirects=False, headers=headers)
        response_headers = response.headers
        status_code = response.status_code

        if(status_code == 200 and first_xml_header or second_xml_header in response_headers):
            data = xmltodict.parse(response.content)
            joomla_version = data["extension"]["version"]

            print(f"[green][INF] Joomla version detected: {joomla_version}\n")
            files_finder(args)
        else:
            print(f"[red][ERR] Can't detect Joomla version on 1° check... [/]")
            get_joomla_version_2(args)

    except requests.exceptions.ConnectionError:
        return print(f'\n[red][ERR] Connection problems with {manifest_path}[/]')
    except xmltodict.expat.ExpatError:
        return print(f"[red][ERR] Can't parse Joomla XML, stopping... \n[/]")
    except KeyError:
        return print(f'\n[red][ERR] Possible false positve on Joomla detection.[/]')
    

def get_joomla_version_2(args):
    language_path = f'{args.u}/language/en-GB/en-GB.xml'

    try:
        response = requests.get(language_path, verify=False, timeout=10, allow_redirects=False, headers=headers)
        response_headers = response.headers
        status_code = response.status_code

        if(status_code == 200 and first_xml_header or second_xml_header in response_headers):
            data = xmltodict.parse(response.content)
            joomla_version = data["metafile"]["version"]

            print(f"[green][INF] Joomla version found: {joomla_version} on second check\n")
            files_finder(args)
        else:
            return print(f"[red][ERR] Can't detect Joomla version on 2° check, stopping... [/]")
            
    except requests.exceptions.ConnectionError:
        return print(f'\n[red][ERR] Connection problems with {language_path}[/]')
    except xmltodict.expat.ExpatError:
        return print(f"[red][ERR] Can't parse Joomla XML, stopping... \n[/]")
    except KeyError:
        return print(f'\n[red][ERR] Possible false positve on Joomla detection.[/]')