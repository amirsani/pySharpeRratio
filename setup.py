# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pypandoc

setup(
    name='pysharperratio',
    version='0.01.01',
    description='A moment-free estimator of the Sharpe (signal-to-noise) ratio.',
    long_description=pypandoc.convert('README.md', 'rst'),
    author='Amir Sani',
    author_email='reachme@amirsani.com',
    url='https://github.com/amirsani/pySharpeRratio', 
    packages=find_packages(exclude=('tests', 'docs')),
    data_files = [("", ["LICENSE"])]
)

