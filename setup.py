# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='pysharperratio',
    version='0.01.11',
    description='A moment-free estimator of the Sharpe (signal-to-noise) ratio.',
    long_description=readme(),
    author='Amir Sani',
    url='http://www.amirsani.com',
    author_email='reachme@amirsani.com',
    download_url='https://github.com/amirsani/pySharpeRratio',
    # packages=['pysharperratio'],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    #
    # Include additional files into the package
    include_package_data=True,
    package_data={'pysharperratio': ['../*.pkl']},
    zip_safe=False
)
