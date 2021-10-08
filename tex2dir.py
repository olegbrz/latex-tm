#!/usr/bin/env python3

import os
import argparse
from typing import Dict, List
from distutils.dir_util import copy_tree
import json

TEMPLATES_DIR = ""


def main():
    parser = argparse.ArgumentParser(prog='tex2dir',
                                     description='Copy LaTeX templates to desired directory.')

    parser.add_argument(
        '-p', '--path', help='Target directory of LaTeX template.')

    parser.add_argument(
        '-t', '--template', help='Which template has to be copied to the directory.')

    args = parser.parse_args()


def directory_is_valid(folder_path: str) -> bool:
    target_file = os.path.join(folder_path, "template_data.json")
    return os.path.exists(target_file)


def get_templates_directories() -> List[str]:
    folders_in_template_directory = [os.path.join(TEMPLATES_DIR, folder)
                                     for folder in os.listdir(TEMPLATES_DIR)
                                     if os.path.isdir(os.path.join(TEMPLATES_DIR, folder))]

    # Filter only valid directories (with template_data.json file inside)
    template_folders_paths = list(
        filter(directory_is_valid, folders_in_template_directory))

    return template_folders_paths


def import_template(template_path: str, target_path: str):
    copy_tree(template_path, target_path)


def get_template_data(template_path: str) -> Dict:
    with open(os.path.join(template_path, 'template_data.json')) as d:
        template_data = json.load(d)

    return template_data


def list_templates():
    directories = get_templates_directories()
    templates_data = []

    for directory in directories:
        templates_data.append(get_template_data(directory))
    return templates_data


def print_templates():
    templates_data = list_templates()
    print(f'{"Short name":<20}{"Name":<30}Type')
    print('='*80)
    for template in templates_data:
        print(
            f'{template["short_name"]:<20}{template["name"]:<30}{template["type"]}')


def get_template_path(template_short_name):
    for directory in get_templates_directories():
        short_name = get_template_data(directory)['short_name']
        if template_short_name == short_name:
            return directory


if __name__ == '__main__':
    main()
