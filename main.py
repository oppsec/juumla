#!/usr/bin/env python3

from design.ui import clear, get_banner
from lib.detect import connect

from argparse import ArgumentParser


def main() -> None:

    clear()
    get_banner()

    parser = ArgumentParser()
    parser.add_argument('-u', help='Website URL to run Juumla', required=True)
    args = parser.parse_args()

    connect(args)


main()