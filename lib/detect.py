from rich import print

from requests import get, exceptions

from urllib3 import disable_warnings
disable_warnings()

from lib.version import get_joomla_version
from lib.manager import props

from lib.info import *


def connect(args: str) -> str:
    """
    Try to connect to the target
    """

    try:
        response = get(args.u, **props)
        status_code = response.status_code

        verify = lambda success = 200: status_code == success
        (first_check(args)) if verify() else print(f"[red][ERR] Connection problems with {args.u} | {status_code} [/]")

    except exceptions.ConnectionError as e:
        return print(f"[red][ERR] Connection problems with {args.u} | {e} [/]")

    except exceptions.MissingSchema:
        return print(f"[red][ERR] Invalid URL, did you mean https://{args.u}?")


def first_check(args: str) -> str:

    print(joomla_check)

    url = f"{args.u}{joomla_admin_path}"
    text = "Joomla!"

    try:
        response = get(url, **props)
        body = response.text
        status_code = response.status_code

        verify = lambda success = 200: status_code == success and text in body

        if(verify()):
            print(success_first)
            get_joomla_version(args)
        else:
            print(fail_first)
            second_check(args)

    except exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e} [/]')


def second_check(args:str) -> str:

    url = f"{args.u}{joomla_admin_logo_path}"

    try:
        response = get(url, **props)
        status_code = response.status_code

        verify = lambda success = 200: status_code == success

        if(verify()):
            print(success_second)
            get_joomla_version(args)
        else:
            print(fail_second)
            third_check(args)

    except exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {url} | {e} [/]')


def third_check(args: str) -> str:

    url = f"{args.u}{robots_file}"

    signature = "Joomla"
    content = "/components"

    try:
        response = get(url, **props)
        status_code = response.status_code
        body = response.text

        verify = lambda success = 200: status_code == success and signature or content in body

        if(verify()):
            print(success_third)
            get_joomla_version(args)
        else:
            print(fail_third)
            fourth_check(args)

    except exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {url} | {e} [/]')


def fourth_check(args: str) -> str:

    content = '<meta name="generator" content="Joomla"'

    try:
        response = get(args.u, **props)
        status_code = response.status_code
        body = response.text

        verify = lambda success = 200: status_code == success and content in body

        if(verify()):
            print(success_fourth)
            get_joomla_version(args)
        else:
            print(fail_fourth)
            fifth_check(args)
            
    except exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e} [/]')


def fifth_check(args: str) -> str:
    
    content = "/index.php?option=com_search"

    try:
        response = get(args.u, **props)
        status_code = response.status_code
        body = response.text

        verify = lambda success = 200: status_code == success and content in body

        if(verify()):
            print(success_fifth)
            get_joomla_version(args)
        else:
            return print(not_detected)
            
    except exceptions.ConnectionError as e:
        return print(f'[red][ERR] Connection problems with {args.u} | {e} [/]')