#!/usr/bin/env python3

from io import DEFAULT_BUFFER_SIZE
import os
import sys
import argparse
from typing import Dict, List
from distutils.dir_util import copy_tree
import json

TEMPLATES_DIR = ""

DEFAULT_TEMPLATE_DATA = {"name": "", "short_name": "", "type": ""}


def main():
    parser = argparse.ArgumentParser(
        prog="tex2dir", description="Copy LaTeX templates to desired directory."
    )

    parser.add_argument(
        "-p",
        "--path",
        help="Target directory of LaTeX template. Defaults to current working directory.",
        default=os.path.abspath(os.getcwd()),
    )

    parser.add_argument(
        "-t", "--template", help="Which template has to be copied to the directory."
    )

    parser.add_argument(
        "-L", "--list", help="List all available templates", action="store_true"
    )

    parser.add_argument(
        "-I",
        "--init",
        help="Initializes a directory as LaTeX template (generates JSON data file that you will have to fill).",
        action="store_true",
    )

    args = parser.parse_args()

    if args.init:
        init_directory(args.path)
    elif args.list:
        print_templates()
    elif args.template:
        target_template_path = get_template_path(args.template)
        import_template(target_template_path, os.path.abspath(args.path))
    else:
        parser.print_help(sys.stderr)


def directory_is_valid(folder_path: str) -> bool:
    """directory_is_valid checks if a directory is a valid template directory.
    A directory is valid if "template_data.json" file is inside.

    Args:
        folder_path (str)

    Returns:
        bool
    """
    target_file = os.path.join(folder_path, "template_data.json")
    return os.path.exists(target_file)


def get_templates_directories() -> List[str]:
    """get_templates_directories gets all directories in specified templates
    directory, and filters only valid template directories.

    Returns:
        List[str]: valid directories paths.
    """
    folders_in_template_directory = [
        os.path.join(TEMPLATES_DIR, folder)
        for folder in os.listdir(TEMPLATES_DIR)
        if os.path.isdir(os.path.join(TEMPLATES_DIR, folder))
    ]

    # Filter only valid directories (with template_data.json file inside)
    template_folders_paths = list(
        filter(directory_is_valid, folders_in_template_directory)
    )

    return template_folders_paths


def import_template(template_path: str, target_path: str):
    """import_template copies template to a specified path.

    Args:
        template_path (str)
        target_path (str)
    """
    copy_tree(template_path, target_path)
    os.remove(target_path + "/template_data.json")
    print("Template imported successfully!")


def get_template_data(template_path: str) -> Dict:
    """get_template_data reads template data.

    Args:
        template_path (str)

    Returns:
        Dict: JSON parsed to dictionary.
    """
    with open(os.path.join(template_path, "template_data.json")) as d:
        template_data = json.load(d)

    return template_data


def list_templates() -> List[Dict]:
    """list_templates reads all templates data.

    Returns:
        List[Dict]: all templates data listed as dictionaries.
    """
    directories = get_templates_directories()
    templates_data = []

    for directory in directories:
        templates_data.append(get_template_data(directory))
    return templates_data


def print_templates():
    """print_templates prints all available templates data in a human readable way."""
    templates_data = list_templates()
    print(f'{"Short name":<20}{"Name":<30}Type')
    print("=" * 80)
    for template in templates_data:
        print(f'{template["short_name"]:<20}{template["name"]:<30}{template["type"]}')


def get_template_path(template_short_name: str) -> str:
    """get_template_path iterates over all template directories searching the
    specified template.

    Args:
        template_short_name (str)

    Returns:
        str: target template path.
    """
    for directory in get_templates_directories():
        short_name = get_template_data(directory)["short_name"]
        if template_short_name == short_name:
            return directory


def init_directory(directory_path: str):
    with open(directory_path + "/template_data.json", "w") as td:
        json.dump(DEFAULT_TEMPLATE_DATA, td)
    print('Template initialized successfully. Please, fill "template_data.json" file.')


if __name__ == "__main__":
    main()
