#!/usr/bin/env python

import subprocess
import os.path

NOTEBOOKS_DIR = 'notebooks'
SKIP_NOTEBOOKS = [os.path.join('Bonus', 'What to do when things go wrong.ipynb'),
                  os.path.join('AWIPS', 'AWIPS_Grids_and_Cartopy.ipynb'),
                  os.path.join('AWIPS', 'Grid_Levels_and_Parameters.ipynb'),
                  os.path.join('AWIPS', 'Map_Resources_and_Topography.ipynb'),
                  os.path.join('AWIPS', 'Model_Sounding_Data.ipynb'),
                  os.path.join('AWIPS', 'NEXRAD_Level_3_Plot_with_Matplotlib.ipynb'),
                  os.path.join('AWIPS', 'Satellite_Imagery.ipynb'),
                  os.path.join('AWIPS', 'Upper_Air_BUFR_Soundings.ipynb'),
                  os.path.join('AWIPS', 'Watch_and_Warning_Polygons.ipynb')]


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
