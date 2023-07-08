#!/usr/bin/env python3

from src.interface.ui import get_banner
from src.juumla.main import perform_checks

from argparse import ArgumentParser

if __name__ == "__main__":
    get_banner()

    parser = ArgumentParser()
    parser.add_argument('-u', help='-u: HTTP(s) target URL to run the scanner', required=True)
    args = parser.parse_args()

    perform_checks(args)