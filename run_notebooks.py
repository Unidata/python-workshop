#!/usr/bin/env python

import subprocess
import os.path

NOTEBOOKS_DIR = 'notebooks'
SKIP_NOTEBOOKS = [os.path.join('Bonus','What to do when things go wrong.ipynb'),
                  os.path.join('python-awips',
                                'NEXRAD3_Storm_Total_Accumulation.ipynb'),
                  os.path.join('python-awips',
                                'Watch_and_Warning_Polygons.ipynb'),
                  os.path.join('python-awips',
                               'NEXRAD3_Reflectivity_Velocity_Matplotlib.ipynb'),
                  os.path.join('python-awips',
                               'Satellite_Imagery.ipynb')]


def run_notebook(notebook):
    args = ['jupyter', 'nbconvert', '--execute',
            '--ExecutePreprocessor.timeout=900',
            '--ExecutePreprocessor.kernel_name=python3',
            '--to=notebook', '--stdout']

    args.append(notebook)
    with subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=None) as proc:
        proc.wait()
        return proc.returncode

results = []
def log_result(result):
    results.append(result)

if __name__ == '__main__':
    import glob
    import multiprocessing as mp
    import sys

    ret = 0
    notebooks = set(glob.glob(os.path.join(NOTEBOOKS_DIR, '**', '*.ipynb'), recursive=True))
    notebooks -= set(os.path.join(NOTEBOOKS_DIR, s)
                     for s in SKIP_NOTEBOOKS)

    with mp.Pool(processes=6) as pool:
        for notebook in notebooks:
            pool.apply_async(run_notebook, args=(notebook,), callback=log_result)
        pool.close()
        pool.join()

    ret = max(results)
    sys.exit(ret)
