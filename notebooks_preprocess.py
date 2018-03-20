#!/usr/bin/env python

import json
import re
from pathlib import Path

def get_cell_content_as_string(cell):
    """Return the cells source as a single string."""
    return ''.join(cell['source']) + '\n'


def process_cell(path, cell):
    """Replace the solution button with the solution code."""
    modified = False

    # See if there is a solution div in the cell
    for cell_source_line in cell['source']:
        m = re.match('<div id="sol*', cell_source_line)
        if m:
            modified = True
            # Breakout the solution content (i.e. strip HTML)
            solution_code = get_cell_content_as_string(cell)
            solution_code = solution_code.split('```python')[1]
            solution_code = solution_code.rsplit('```', maxsplit=1)[0]

            # Replace the cell content and change it to a code cell.
            cell['cell_type'] = "code"
            cell['source'] = "# Replaced by notebook preprocessor\n" + solution_code
            cell['outputs'] = []
            cell['execution_count'] = 0

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
