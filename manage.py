#!/usr/bin/env python
"""Bot command-line utility for administrative tasks."""
import os
import sys

from core.management import execute_from_command_line


def main():
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
