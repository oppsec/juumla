#!/usr/bin/env python3

from src.interface.ui import clear, banner
from src.juumla.main import start

from argparse import ArgumentParser

if __name__ == "__main__":
    clear()
    banner()

    parser: str = ArgumentParser()
    parser.add_argument('-u', help='Target URL to run Juumla', required=True)
    args: str   = parser.parse_args()

    start(args)