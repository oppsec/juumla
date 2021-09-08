#!/usr/bin/env python3

from src.interface.ui import banner
from src.juumla.main import start

from argparse import ArgumentParser

if __name__ == "__main__":
    banner()

    parser: str = ArgumentParser()
    parser.add_argument('-u', help='Run Juumla on target', required=True)
    args: str = parser.parse_args()

    start(args)