#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from setuptools import setup

setup(
    name = 'my_app',
    version = '0.1.0',
    lincense = 'GNU General Public License v3',
    author = 'Christopher Farrugia',
    author_email = 'foxcode9@gmail.com',
    description = 'Hello world application for Flask',
    packages = ['my_app'],
    platform = 'any',
    install_requires = [
        'Flask==1.1.2',
        'python-dotenv==0.14.0'
    ]
)