import re
from rich import print

from requests import get, exceptions
from urllib3 import disable_warnings
disable_warnings()

from lib.files import files_finder
from lib.manager import props
from lib.info import *

from xmltodict import parse, expat


first_xml_header = 'application/xml'
second_xml_header = 'text/xml'

def get_joomla_version(args: str) -> str:

    print(version_check)

    url = f'{args.u}{manifest_joomla}'

    try:
        response = get(url, **props)
        response_headers = response.headers
        status_code = response.status_code

        if(status_code == 200 and first_xml_header or second_xml_header in response_headers):
            data = parse(response.content)
            joomla_version = data["extension"]["version"]

            print(f"[green][INF] Joomla version detected: {joomla_version} on 1° check\n")
            files_finder(args)
        else:
            print(fail_version_first)
            get_joomla_version_2(args)

    except exceptions.ConnectionError:
        return print(f'\n[red][ERR] Connection problems with {url}[/]')
    except expat.ExpatError:
        return print(xml_parse)
    except KeyError:
        return print(false_positive)
    

def get_joomla_version_2(args: str) -> str:
    
    url = f"{args.u}{language_joomla}"

    try:
        response = get(url, **props)
        response_headers = response.headers
        status_code = response.status_code

        if(status_code == 200 and first_xml_header or second_xml_header in response_headers):
            data = parse(response.content)
            joomla_version = data["metafile"]["version"]

            print(f"[green][INF] Joomla version found: {joomla_version} on 2° check\n")
            files_finder(args)
        else:
            return print(fail_version_second)
            
    except exceptions.ConnectionError:
        return print(f'\n[red][ERR] Connection problems with {url} [/]')
    except expat.ExpatError:
        return print(xml_parse)
    except KeyError:
        return print(false_positive)