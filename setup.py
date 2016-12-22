#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pandas',
    'tables',
    'decorator',
    'plugnparse'
]

test_requirements = [
    'tox'
]

setup(
    name='wolong',
    version='0.0.1',
    description="Pandas in captivity. Base classes and API for rapid prototyping high-throughput batch processors and their CLIs.",
    long_description=readme + '\n\n' + history,
    author="Brian Rossa",
    author_email='brian.rossa@gmail.com',
    url='https://github.com/brianthelion/wolong',
    packages=[
        'wolong',
    ],
    package_dir={'wolong':
                 'wolong'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='wolong',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    dependency_links=[
        'https://github.com/brianthelion/plugnparse/tarball/master#egg=plugnparse'
    ]
)
