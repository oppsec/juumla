from json import load
from rich import print

from src.juumla.modules.files import files_manager

def vuln_manager(args, version) -> None:
    """ Search for vulnerabilities on current target Joomla version """

    print("\n[cyan][INF] Searching for Joomla vulnerabilites for this version [/]")

    filename: str = "src/juumla/data/vulnerabilites.json"
    with open(filename) as file:
        content = load(file)
        
        for vuln_title, vuln_version in content.items():

            if version <= vuln_version:
                print(f"[green][INF] {vuln_title} [/]")
            else:
                pass


    print("[yellow][WRN] Finished Joomla vulnerabilities scanner... [/]")
    files_manager(args)