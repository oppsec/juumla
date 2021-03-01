from rich import print

def get_banner():
    with open('design/banner.txt') as file:
        content = file.read()
        print(f"[yellow]{content}[/]")