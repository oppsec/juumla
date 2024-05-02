from json import load
from rich.console import Console
console = Console()

from src.juumla.modules.files import files_manager


def vuln_manager(url, version) -> None:
    " Search for vulnerabilities on current target Joomla version "

    console.print("\n[yellow][!][/] Running Joomla vulnerabilities scanner! [cyan](2/3)[/]", highlight=False)

    filename: str = "src/juumla/data/vulnerabilites.json"
    
    with open(filename) as file:
        content = load(file)

        for vuln_title, vuln_version in content.items():
            vuln_version = vuln_version.split("|")
            min_version = vuln_version[0]
            max_version = vuln_version[1]

            if version >= min_version and version <= max_version:
                console.print(f"[green][+][/] {vuln_title}", highlight=False)
            else:
                pass

    console.print("[yellow][!][/] Vulnerabilities scanner finished! [cyan](2/3)[/]", highlight=False)
    files_manager(url)