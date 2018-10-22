#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('requirements/main.in') as requirements_file:
    requirements = [line.strip()
                    for line in requirements_file
                    if line.strip() and line.strip()[0] not in "-#"]

test_requirements = [
    'pytest',
]

setup_requirements = [
    'pytest-runner',
    'sphinx',
    'wheel',
]

setup(
    name='nlsummary-utils',
    version='0.1.0a',
    description="Simple package to facilitate the summary of large texts to smaller, concise ideas.",
    long_description=readme + '\n\n' + history,
    author="Mark Liederbach",
    author_email='usrolh@tdstelecom.com',
    url='https://wiki.tds.net/display/admnetapps/nlsummary-utils',
    packages=find_packages(include=[
        'nlsummary_utils',
    ]),
    include_package_data=True,
    install_requires=requirements,
    
    license="All Rights Reserved",
    zip_safe=False,
    keywords='nlsummary_utils',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
