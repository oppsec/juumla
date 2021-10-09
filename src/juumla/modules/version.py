from requests import get, exceptions
from urllib3 import disable_warnings
from xmltodict import parse, expat
from rich import print

from src.juumla.settings import props
from src.juumla.modules.vulns import vuln_manager

disable_warnings()

app_xml_header = "application/xml"
text_xml_header = "text/xml"


def get_version(args) -> None:
    """ Try to get Joomla target version """

    print("\n[cyan][-] Started version detector... [1/3] [/]")

    xml_file = f"{args.u}/language/en-GB/en-GB.xml"

    try:
        response: str = get(xml_file, **props)
        status_code: str = response.status_code
        headers: str = response.headers

        if status_code == 200 and app_xml_header or text_xml_header in headers:
            data = parse(response.content)
            version = data["metafile"]["version"]

            print(f"[green][+] Joomla version is: {version} [/]")
            vuln_manager(args, version)

        else:
            print("[yellow][!] Couldn't get Joomla version, trying other way... [/]")
            last_version_try(args)

    except exceptions.ConnectionError:
        return print(f'\n[red][-] Connection problems with {xml_file}[/]')
    except expat.ExpatError:
        return print(f"\n[red][-] Couldn't get Joomla version, stopping... [/]")
    except KeyError:
        return print(f"\n[red][-] Possible false positive, stopping... [/]")


def last_version_try(args) -> None:
    """ Last try to get Joomla version """

    manifest_file = f"{args.u}/administrator/manifests/files/joomla.xml"

    try:
        response = get(manifest_file, **props)
        status_code = response.status_code
        headers = response.headers

        if status_code == 200 and app_xml_header or text_xml_header in headers:
            data = parse(response.content)
            version = data["extesion"]["version"]

            print(f"[green][+] Joomla version is: {version} [/]")
            vuln_manager(args, version)

        else:
            return print("[yellow][!] Couldn't get Joomla version, stopping... [/]")

    except exceptions.ConnectionError:
        return print(f'\n[red][-] Connection problems with {manifest_file}[/]')
    except expat.ExpatError:
        return print(f"\n[red][-] Couldn't get Joomla version, stopping... [/]")
    except KeyError:
        return print(f"\n[red][-] Possible false positive, stopping... [/]")

