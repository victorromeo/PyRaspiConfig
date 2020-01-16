from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PyRaspiConfig',
    version='0.1.0',
    description='Python wrapper for Raspi-Config',
    long_description=readme,
    author='victorromeo',
    author_email='victorromeo@github.com',
    url='https://github.com/victorromeo/PyRaspiConfig',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
