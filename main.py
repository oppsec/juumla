#!/usr/bin/env python3

from design.banner import get_banner
from design.clear import clear

from lib.checker import connection_check

import argparse

def main():
    clear()
    get_banner()

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='Target URL', type=str)
    args = parser.parse_args()

    connection_check(args)

if __name__ == "__main__":
    main()