#!/usr/bin/env python3
"""nonpremes-python-ykaw."""
import sys,argparse
from utils import timestamp
def main():
    p=argparse.ArgumentParser(description="nonpremes-python-ykaw")
    p.add_argument("--version",action="version",version="1.0.0")
    p.add_argument("-v","--verbose",action="store_true")
    a=p.parse_args()
    if a.verbose:print(f"[{timestamp()}] nonpremes-python-ykaw v1.0.0")
    print(f"Hello from nonpremes-python-ykaw!")
    return 0
if __name__=="__main__":sys.exit(main())
