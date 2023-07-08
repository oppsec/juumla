from requests import get, exceptions
from urllib3 import disable_warnings
from xmltodict import parse, expat
from rich import print

from src.juumla.settings import props
from src.juumla.modules.vulns import vuln_manager

disable_warnings()

app_xml_header = "application/xml"
text_xml_header = "text/xml"


def get_version(url: str) -> None:
    " Get Joomla version based on XML files response "

    print("\n[cyan]> Running Joomla version scanner... [1/3] [/]")

    xml_file = f"{url}/language/en-GB/en-GB.xml"

    try:
        response: str = get(xml_file, **props)
        headers: str = response.headers

        if response.ok and app_xml_header or text_xml_header in headers:
            data = parse(response.content)
            version = data["metafile"]["version"]

            print(f"[green]> Joomla version is: {version} [/]")
            vuln_manager(url, version)
        else:
            print("[yellow]> Couldn't get Joomla version, trying other way... [/]")
            get_version_second(url)

    except Exception as error:
        print(f"[red]> Error when trying to get Joomla version on {url} | {error} [/]")
        return True


def get_version_second(url) -> None:
    """ Last try to get Joomla version """

    manifest_file = f"{url}/administrator/manifests/files/joomla.xml"

    try:
        response = get(manifest_file, **props)
        headers = response.headers

        if response.ok and app_xml_header or text_xml_header in headers:
            data = parse(response.content)
            version = data["extension"]["version"]

            print(f"[green]> Joomla version is: {version} [/]")
            vuln_manager(url, version)
        else:
            print("[yellow]> Couldn't get Joomla version, stopping... [/]")
            return True

    except Exception as error:
        print(f"[red]> Error: {error} [/]")
        return True