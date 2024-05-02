from requests import get, exceptions

from rich.console import Console
console = Console()

from urllib3 import disable_warnings
disable_warnings()

from src.juumla.settings import props
from src.juumla.modules.version import get_version


def perform_checks(args) -> None:
    " Connect to the target and check if status code is positive "

    global url
    url = args.u

    try:
        response: str = get(url, **props)
        status_code: int = response.status_code
        body: str = response.text

        if response.ok:
            console.print(f"[green][+][/] Connected successfully to [yellow]{url}[/]", highlight=False)
            detect_joomla(body)
        else:
            console.print(f"[red][-][/] Host returned status code: {status_code}", highlight=False)
            return

    except exceptions as error:
        console.print(f"[red][-][/] Error when trying to connect to {url}: {error}", highlight=False)
        return


def detect_joomla(body) -> None:
    " Check if meta tag 'generator' contains Joomla! in body response "

    console.print("[yellow][!][/] Checking if target is running Joomla...", highlight=False)

    if '<meta name="generator" content="Joomla!' in body: 
        get_version(url)
    else:
        console.print("[red][-][/] Target is not running Joomla apparently")
        return