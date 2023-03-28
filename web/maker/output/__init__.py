import os
import shutil

from cookiecutter.main import cookiecutter

BASE_PATH = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(BASE_PATH, 'output')


def make_template(context, path):
    template = os.path.join(BASE_PATH, path)
    result = cookiecutter(template, no_input=True, output_dir=OUTPUT_DIR, extra_context=context)
    filename = result.split('\\')[-1]
    zipped = shutil.make_archive(f'{OUTPUT_DIR}\{filename}', 'zip', result)
    shutil.rmtree(result)
    with open(zipped, 'rb') as f:
        file = f.read()
    return file
