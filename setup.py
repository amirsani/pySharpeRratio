# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='pysharperratio',
    version='0.01.01',
    description='A moment-free estimator of the Sharpe (signal-to-noise) ratio.',
    long_description=readme(),
    author='Amir Sani',
    author_email='reachme@amirsani.com',
    url='https://github.com/amirsani/pySharpeRratio', 
    data_files = [("", ["LICENSE"])]
)

