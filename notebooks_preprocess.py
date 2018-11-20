#!/usr/bin/env python

import json
import re
import sys
import warnings
from pathlib import Path

def get_cell_content_as_string(cell):
    """Return the cells source as a single string."""
    return ''.join(cell['source']) + '\n'


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


def find_extra_content(cell_text):
    """Find and non load magic or blank lines in a solution cell."""
    for line in cell_text.split('\n'):
        m = re.match('#\s?%load.*', line)
        if not m and line:
            raise RuntimeError('Solution cell has extra content: {}'.format(cell_text))


def check_if_notebook_has_run(cell):
    """Check to ensure that the notebook has not been committed in a run state."""
    for cell in json_data['cells']:
        if cell['cell_type']=='code' and cell['execution_count'] != None:
            return True
    return False

def process_cell(path, cell):
    """Replace solution button and load magics in cells"""
    buttons_replaced = process_buttons(path, cell)
    load_magic_replaced = process_load_magic(path, cell)
    if buttons_replaced or load_magic_replaced:
        modified_cell = True
    else:
        modified_cell = False
    return modified_cell


def process_load_magic(path, cell):
    """Replace load magics with the solution."""
    modified = False
    # Find any load magics
    load_magics = find_load_magics_in_cell(cell)

    # Replace load magics with file contents
    for magic_string in load_magics:
        path = Path(path)
        script_path = path.parent / magic_string.split('load ')[1]
        formatted_script = format_script_for_cell(script_path)
        cell_str = get_cell_content_as_string(cell)
        find_extra_content(cell_str)
        cell['source'] = cell_str + formatted_script
        modified = True

    return modified

def process_buttons(path, cell):
    """Replace the solution button with the solution code."""
    modified = False

    # See if there is a solution div in the cell
    for cell_source_line in cell['source']:
        m = re.match('<div id="sol*', cell_source_line)
        if m:
            modified = True
            # Breakout the solution content (i.e. strip HTML)
            solution_code = get_cell_content_as_string(cell)
            solution_code = solution_code.split('<code><pre>')[1]
            solution_code = solution_code.rsplit('</pre></code>\n</div>', maxsplit=1)[0]

            # Replace any escaped characters with the character to avoid markdown
            # escapes (See issue #323)
            solution_code = solution_code.replace('\\#', '#')

            # Replace the cell content and change it to a code cell.
            cell['cell_type'] = "code"
            cell['source'] = "# Replaced by notebook preprocessor\n" + solution_code
            cell['outputs'] = []
            cell['execution_count'] = 0

    return modified


# Recursively grab all notebooks and process them
notebooks = Path('notebooks').rglob('*.ipynb')
notebooks_that_have_run = []
for notebook in notebooks:
    if not str(notebook.parts[-2]).startswith('.'):
        modified = False
        # Read in the notebook as JSON data
        print('Reading notebook: {}'.format(notebook))
        with open(str(notebook), 'r', encoding='utf8') as f:
            json_data = json.load(f)

        # Check the notebook for executed code cells - we don't want those.
        found_executed_cells = check_if_notebook_has_run(json_data)
        if found_executed_cells:
            notebooks_that_have_run.append(notebook)

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

if len(notebooks_that_have_run) > 0:
    print('These notebooks were committed in the executed state: ',
          notebooks_that_have_run)
    sys.exit(1)
