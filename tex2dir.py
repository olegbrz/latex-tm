#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser(prog='tex2dir',
                                 description='Copy LaTeX templates to desired directory.')

parser.add_argument('-p', '--path', help='Target directory of LaTeX template.')

parser.add_argument(
    '-t', '--template', help='Which template has to be copied to the directory.')

args = parser.parse_args()
