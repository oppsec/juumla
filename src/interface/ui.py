from rich import print


def banner() -> str:
    """ Return the Juumla banner from banner.txt file """

    filename: str = "src/interface/banner.txt"
    
    with open(filename) as file:
        content: str = file.read()

        return print(f"[bold yellow]{content}[/]")