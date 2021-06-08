from rich import print
from os import system, name

def read_banner_file() -> str:
    """
    Get the banner.txt content and return
    """

    with open('design/banner.txt') as banner_file:
        file_content = banner_file.read()
        return f"[yellow]{file_content} [/]"


def get_banner() -> str:
    """
    Print the banner.txt content
    """
    
    return print(read_banner_file())


def clear() -> None:
    """
    Clear the screen
    """

    system('cls' if name == 'nt' else 'clear')