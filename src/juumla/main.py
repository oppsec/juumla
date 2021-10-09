from requests import get, exceptions
from rich import box, print
from rich.table import Table
from urllib3 import disable_warnings

from src.juumla.settings import props, get_today_date
from src.juumla.modules.version import get_version

disable_warnings()


def start(args) -> None:
    " Check if host address is alive to start Juumla "

    # Generate information table
    table = Table(title="", box=box.SQUARE)

    table.add_column("Version", justify="center", style="yellow")
    table.add_column("Target", justify="center", style="yellow")
    table.add_column("Date", justify="center", style="yellow")

    table.add_row("build: 0.1.3", f"{args.u}", f"{get_today_date}")

    print(table)

    try:

        response: str = get(args.u, **props)
        status_code: str = response.status_code
        body: str = response.text

        check = lambda success = 200: status_code == success
        (detect_joomla(args, body)) if check() else print(f"[red][-] Returned status code: {status_code} [/]")

    except exceptions.ConnectionError as error:
        return print(f"[red][-] Connection problems with {args.u} | {error} [/]")

    except exceptions.MissingSchema as error:
        return print(f"[red][-] Invalid URL, try with: http(s)://{args.u} [/]")

    except exceptions.InvalidURL as error:
        return print(f"[red][-] Invalid URL... | {error} [/]")


def detect_joomla(args, body) -> None:
    " Try to detect if target is actually running Joomla CMS "

    print("\n[yellow][!] Checking if target is running Joomla... [/]")

    basic = "Joomla"
    meta = '<meta name="generator" content="Joomla'
    csrf_token = "'X-CSRF-Token': Joomla.getOptions('csrf.token')"
    script_type = "joomla-script-options"

    if basic or meta or csrf_token or script_type in body:
        print("[green][+] Target is running Joomla [/]")
        get_version(args)

    else:
        return print("[red][-] Target is not running Joomla apparently [/]")