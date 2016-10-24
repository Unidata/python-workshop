#!/usr/bin/env python

import subprocess

NOTEBOOKS_DIR = 'notebooks'
SKIP_NOTEBOOKS = ['What to do when things go wrong.ipynb']


def run_notebook(notebook):
    args = ['jupyter', 'nbconvert', '--execute',
            '--ExecutePreprocessor.timeout=300',
            '--ExecutePreprocessor.kernel_name=workshop',
            '--to=notebook', '--stdout']

    args.append(notebook)
    with subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=None) as proc:
        proc.wait()
        return proc.returncode


if __name__ == '__main__':
    import glob
    import os.path
    import sys

    ret = 0
    notebooks = set(glob.glob(os.path.join(NOTEBOOKS_DIR, '*.ipynb')))
    notebooks -= set(os.path.join(NOTEBOOKS_DIR, s)
                     for s in SKIP_NOTEBOOKS)
    for path in sorted(notebooks):
        ret = max(run_notebook(path), ret)
    sys.exit(ret)
