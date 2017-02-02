# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pypandoc

setup(
    name='sharpeRratio',
    version='0.05',
    description='A moment-free estimator of the Sharpe (signal-to-noise) ratio.',
    long_description=pypandoc.convert('README.md', 'rst'),
    author='Amir Sani',
    author_email='reachme@amirsani.com',
    url='https://github.com/amirsani/sharpeRratio', 
    packages=find_packages(exclude=('tests', 'docs')),
    data_files = [("", ["LICENSE"])]
)

