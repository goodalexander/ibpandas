#!/usr/bin/env python

import os.path
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    sys.exit()

setup(
    name='ibpandas',
    packages=[],
    description='ib for pandas, pandas for ib',
    long_description='use pandas to interact w the interactive brokers api',
    version=1,
    author='Alex Good',
    author_email='goodalexander@gmail.com',
    url='https://github.com/goodalexander/ibpandas',
    keywords=['interactive-brokers', 'ib-pandas'],
    install_requires=['requests>=2.2.1','pandas>=0.21.1','ibapi>=9.73.6'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    license='MIT'
    )
