#!/usr/bin/env/python
# -*- coding: utf-8 -*-

import unittest
import os
from leafly import metadata
from distutils.cmd import Command
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
    "Topic :: Utilities",
    "License :: OSI Approved :: Apache Software License",
]

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from test_leafly import TestLeaflyAPI
        suite = unittest.TestLoader().loadTestsFromTestCase(TestLeaflyAPI)
        unittest.TextTestRunner(verbosity=2).run(suite)

setup(
    name='leafly',
    version=metadata.__version__,
    url="http://github.com/lionheart/python-leafly",
    description="A Python wrapper for Leafly",
    classifiers=classifiers,
    keywords="leafly",
    license=metadata.__license__,
    author=metadata.__author__,
    author_email=metadata.__email__,
    packages=['leafly'],
    install_requires=["requests>=2.0.0"],
    package_data={'': ['LICENSE', 'README.md']},
    cmdclass={'test': TestCommand},
)

