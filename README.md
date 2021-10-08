# LaTeX Template Manager

When using LaTeX to write documents, most people usually have templates to reuse. The annoying part comes when you write many documents with LaTeX, and each time you have to manually copy the template from some directory where you have it saved.

LaTeX TM aims to solve this problem. All you need to do is to save all templates in a folder, each one with a metadata file. This script will parse the folder for templates and simplify the process of importing the template into a desired folder.

## Usage

To use the script, just save it in `/usr/local/bin` and give it execution permissions:

```bash
chmod +x ./tex2dir.py
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
