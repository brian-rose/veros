#!/usr/bin/env python

"""Copies a Veros setup to another directory"""

import argparse
import os
import shutil

WORKDIR = os.getcwd()
SCRIPTDIR = os.path.realpath(os.path.dirname(__file__))
SETUPDIR = os.path.realpath(os.path.join(SCRIPTDIR, "../setup"))
SETUPS = [setup for setup in os.listdir(SETUPDIR) if os.path.isdir(os.path.join(SETUPDIR, setup))]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("setup", choices=SETUPS, help="Set-up to copy")
    parser.add_argument("target_dir", default=WORKDIR, nargs="?",
                        help="Target directory (defaults to current directory)")
    args = parser.parse_args()
    shutil.copytree(os.path.join(SETUPDIR, args.setup), os.path.join(args.target_dir, args.setup))
