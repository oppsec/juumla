from requests import get, exceptions
from rich import print
from urllib3 import disable_warnings

from src.juumla.settings import props
from src.juumla.modules.version import get_version

disable_warnings()

def start(args) -> None:
    """ Try to connect to the target passed in -u flag """

    try:
        response: str = get(args.u, **props)
        status_code: str = response.status_code
        body: str = response.text

        check = lambda success = 200: status_code == success
        (detect_joomla(args, body)) if check() else print(f"[red][-] Website returned a status code different than 200 | {status_code} [/]")

    except exceptions.ConnectionError as error:
        return print(f"[red][-] Connection problems with {args.u} | {error} [/]")

    except exceptions.MissingSchema as error:
        return print(f"[red][-] Invalid URL, try with: http(s)://{args.u}")

    except exceptions.InvalidURL:
        return print(f"[red][-] Invalid URL, please check your URL.")


def detect_joomla(args, body) -> None:
    """ Try to detect Joomla on target """

    print("[yellow][!] Checking if target is running Joomla... [/]")

    basic = "Joomla"
    meta = """<meta name="generator" content="Joomla"""
    csrf_token = """'X-CSRF-Token': Joomla.getOptions('csrf.token')"""
    script_type = "joomla-script-options"

    if basic or meta or csrf_token or script_type in body:
        print("[green][+] Target is running Joomla! [/]")
        get_version(args)
    else:
        return print("[red][-] Sorry, couldn't detect Joomla on target... [/]")