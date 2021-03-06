# LaTeX Template Manager

When using LaTeX to write documents, most people usually have templates to reuse. The annoying part comes when you write many documents with LaTeX, and each time you have to manually copy the template from some directory where you have it saved.

LaTeX TM aims to solve this problem. All you need to do is to save all templates in a folder, each one with a metadata file. This script will parse the folder for templates and simplify the process of importing the template into a desired folder.

## Installation

To use the script, you can install it in `usr/local/bin` folder, you can perform this automatically with:

```bash
sudo ./install.sh
```

To check if the script was installed, just type:

```bash
tex2dir -h
```

If the usage help appears, the script was installed successfully.

## Usage

To use the script, just save it in `/usr/local/bin` and give it execution permissions:

```bash
sudo chmod +x ./tex2dir.py
```

To see the help, just type:

```bash
tex2dir -h

usage: tex2dir [-h] [-p PATH] [-t TEMPLATE] [-L] [-I]

Copy LaTeX templates to desired directory.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Target directory of LaTeX template. Defaults to current working directory.
  -t TEMPLATE, --template TEMPLATE
                        Which template has to be copied to the directory.
  -L, --list            List all available templates
  -I, --init            Initializes a directory as LaTeX template (generates JSON data file that you will have to fill).
```

### Template data file

Each template directory must have a `template_data.json` file. You can create the file manually, or just type:

```bash
tex2dir --init [--path <path>]
```

This will create the `json` file that will have the following contents:

```json
{
    "name": "Template name",
    "short_name": "short_name identifier for the script",
    "type": "A4, beamer, etc..."
}
```
