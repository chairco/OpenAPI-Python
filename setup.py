#!/usr/bin/env python

"""
Installer for KKBOX SDK
"""

import uuid

from pip.req import parse_requirements  
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import kkbox_developer_sdk as kksdk


def requirements(path):  
    return [str(r.req) for r in parse_requirements(path, session=uuid.uuid1())]


setup(
    name='kkbox_developer_sdk',
    description='KKBOX Open API Developer SDK for Python',
    author=kksdk.__author__,
    author_email=kksdk.__email__,
    version=kksdk.__version__,
    url='https://github.com/KKBOX/OpenAPI-Python',
    download_url='https://github.com/KKBOX/OpenAPI-Python/tarball/v1.0.1',
    packages=find_packages(),
    install_requires=requirements('requirements.txt'),
    extras_require={
            ':python_version=="2.7"': [
                'functools32>=3.2<=3.99',
                'pathlib'
            ],
    },
    keywords=['KKBOX', 'Open', 'API', 'OpenAPI']
)