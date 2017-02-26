#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

USE_GIT_FLAG = "git+"
EGG_NAME_REGEX = re.compile("\#egg\=(.*)\-.*$")

def parse_requirements_line(req_str):
    package_name = None
    url = None
    if req_str.startswith(USE_GIT_FLAG):
        result = re.search(EGG_NAME_REGEX, req_str)
        package_name = result.group(0)
        url = req_str[len(USE_GIT_FLAG):]
    else:
        package_name = req_str
    return package_name, url

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    lines = (line.strip() for line in requirements_file.readlines())
    names_to_urls = dict(parse_requirements_line(line) for line in lines)
    requirements = names_to_urls.keys()
    dependency_links = [v for v in names_to_urls.values() if v is not None]

test_requirements = [
    'tox'
]

packages = find_packages(exclude=["tests"])

setup(
    name='wolong',
    version='0.0.1',
    description="Pandas in captivity. Base classes and API for rapid prototyping high-throughput batch processors and their CLIs.",
    long_description=readme + '\n\n' + history,
    author="Brian Rossa",
    author_email='brian.rossa@gmail.com',
    url='https://github.com/brianthelion/wolong',
    packages=packages,
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
    dependency_links=dependency_links
)
