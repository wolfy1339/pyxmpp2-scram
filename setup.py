#! /usr/bin/env python

import os.path
import sys

from setuptools import setup

version = "2.0alpha2-git"

setup(
    name =      'pyxmpp2_scram',
    version =   version,
    description =   'SCRAM implementation from PyXMPP2',
    author =    'Jacek Konieczny',
    author_email =  'jajcus@jajcus.net',
    maintainer = 'Valentin Lorentz',
    maintainer_email = 'progval+git@progval.net',
    url =       'https://github.com/Jajcus/pyxmpp2',
    classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: POSIX",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.2",
            "Topic :: Communications",
            "Topic :: Communications :: Chat",
            "Topic :: Internet",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    license =   'LGPL',
    install_requires = [],
    packages = [
        'pyxmpp2_scram',
    ],
)
