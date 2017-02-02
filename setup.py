# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pypandoc

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sharpeRratio',
    version='0.01',
    description='A moment-free estimator of the Sharpe (signal-to-noise) ratio.',
    long_description=pypandoc.convert('README.md', 'rst'),
    author='Amir Sani',
    author_email='reachme@amirsani.com',
    url='https://github.com/amirsani/sharpeRratio',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

