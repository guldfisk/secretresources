from setuptools import setup
import os


def package_files(directory):
    paths = []
    for path, directories, file_names in os.walk(directory):
        for filename in file_names:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('secretresources')

setup(
    name = 'secretresources',
    version = '1.0',
    packages = ['secretresources'],
    package_data = {'': extra_files},
)
