#!/usr/bin/env python

import json
import re
from pathlib import Path


def format_script_for_cell(path):
    """Read and format a .py file to be inserted into the json for a cell."""
    header = '\n# Cell content replaced by load magic replacement.\n'
    with open(str(path), encoding='utf8') as f:
        solution = f.read()
        if not solution:
            raise RuntimeError('Solution {} has no content.'.format(path))
        return header + solution


def find_load_magics_in_cell(cell):
    """Find the load magics in a cell and return them as a list."""
    load_magics = []
    for cell_source_line in cell['source']:
        m = re.match('#\s?%load.*', cell_source_line)
        if m:
            load_magics.append(m.group())
    return load_magics


def get_cell_content_as_string(cell):
    """Return the cells source as a single string."""
    return ''.join(cell['source']) + '\n'


def find_extra_content(cell_text):
    """Find and non load magic or blank lines in a solution cell."""
    for line in cell_text.split('\n'):
        m = re.match('#\s?%load.*', line)
        if not m and line:
            raise RuntimeError('Solution cell has extra content: {}'.format(cell_text))


def process_cell(path, cell):
    """Append the data from the load magics into the cell content."""
    modified = False
    # See if there are any load magics used
    load_magics = find_load_magics_in_cell(cell)

    # Replace the load magics with content from their recpective files
    for magic_string in load_magics:
        path = Path(path)
        script_path = path.parent / magic_string.split('load ')[1]
        formatted_script = format_script_for_cell(script_path)
        cell_str = get_cell_content_as_string(cell)
        find_extra_content(cell_str)
        cell['source'] = cell_str + formatted_script
        modified = True
    return modified


# Recursively grab all notebooks and process them
notebooks = Path('notebooks').rglob('*.ipynb')

for notebook in notebooks:
    if not str(notebook.parts[-2]).startswith('.'):
        modified = False
        # Read in the notebook as JSON data
        print('Reading notebook: {}'.format(notebook))
        with open(str(notebook), 'r', encoding='utf8') as f:
            json_data = json.load(f)

        # Process each cell in the file
        for cell in json_data['cells']:
            modified = process_cell(notebook, cell) or modified

        # Write out the modified notebook
        if modified:
            print('Writing notebook: {}\n'.format(notebook))
            with open(str(notebook), 'w', encoding='utf8') as outfile:
                json.dump(json_data, outfile)
        else:
            print('Notebook not modified.\n')
