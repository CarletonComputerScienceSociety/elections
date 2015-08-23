
#!/usr/bin/env python

# This file is part of the Carleton Computer Science Society election 
# server. It is licensed under the MIT permissive free software license.
# See LICENSE.txt.

from setuptools import setup
from os.path import realpath, dirname
from os import chdir
import sys

install_requires = [
    'flask',
    'flask-admin',
    'flask-sqlalchemy',
]

__version__ = '0.1'

setup(
    name='election_server',
    version=__version__,
    description='A server for running elections.',
    license='MIT',
    author='Jack McCracken',
    author_email='jack.mccracken@ccss.carleton.ca',
    url='https://github.com/JackMc/CCSS-ElectionServer',
    packages=[
        'elections',
        ],
    install_requires=install_requires,
    include_package_data=True,
    test_suite='datacats.tests',
    zip_safe=False,
    entry_points="""
        [console_scripts]
        election_server=elections.main:main
        """,
    )
