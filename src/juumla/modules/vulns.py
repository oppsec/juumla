from json import load
from rich import print

from src.juumla.modules.files import files_manager

def vuln_manager(args, version) -> None:
    """ Search for vulnerabilities on current target Joomla version """

    print("\n[cyan][-] Started vulnerabilities scanner... [2/3] [/]")

    filename: str = "src/juumla/data/vulnerabilites.json"
    
    with open(filename) as file:
        content = load(file)

        for vuln_title, vuln_version in content.items():

            vuln_version = vuln_version.split("|")
            min_version = vuln_version[0]
            max_version = vuln_version[1]

            if version >= min_version and version <= max_version:
                print(f"[green][+] {vuln_title} [/]")
            else:
                pass


    print("[yellow][!] Vulnerabilities scanner finished [2/3] [/]")
    files_manager(args)