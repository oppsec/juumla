from rich import print


def banner() -> str:
    " Return application banner from banner.txt file "

    file_path: str = "src/interface/banner.txt"
    
    with open(file_path) as content:
        lines: str = content.read()

        return print(f"[bold yellow]{lines} [/]")