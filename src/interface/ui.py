from rich import print
from os import system, name


def banner() -> None:
    """ Returns the application banner """

    filename: str = "src/interface/banner.txt"
    with open(filename) as file:
        content: str = file.read()

        return print(f"[yellow bold]{content}[/]")


def clear() -> None:
    """ Clear the terminal """

    system('cls' if name == 'nt' else 'clear')