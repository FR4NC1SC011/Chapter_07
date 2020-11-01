#!/usr/bin/python3.8

import os

def run(**args):
    print("[*] In environment module.")
    return str(os.environ)
