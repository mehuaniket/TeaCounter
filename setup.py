#!/usr/bin/env python
from distutils.core import setup

setup(
    name='teacounter',
    version='0.1.0',
    description='tea counter command line tool',
    long_description='''don't raise your hands,instead fire command oon terminal''',
    license='MIT',
    author='Aniket patel',
    author_email='patelaniket@gmail.com',
    url='http://github.com/kodani/teacounter',
    scripts=[
    'tea.py'
    ],
    install_requires=[
       'requests',
       'fire',
    ],
    keywords=['tea count'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: count cmd tool'
    ]
    )