#!/usr/bin/python3
"""read a file that has utf-8"""


def read_file(filename=""):
    """read a text file and print it as stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        for lilne in f:
            print(line, end="")
