#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

requirements = [
    'pyyaml',
    'appdirs'
]

setup(
    name="app-deployer",
    version='v0.1.0',
    description="Deploys all types of applications using Ansible and Ansistrano",
    long_description=readme + '\n\n' + history,
    author="Mike Charles",
    author_email='mike.charles@noaa.gov',
    url="https://github.com/noaa-nws-cpc/app-deployer",
    packages=[
        'app_deployer',
    ],
    package_dir={'app_deployer':
                 'app_deployer'},
    include_package_data=True,
    install_requires=requirements,
    license="CC",
    zip_safe=False,
    keywords='app_deployer',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    ],
    entry_points={
        'console_scripts': [
            "deploy = app_deployer.__main__:main"
        ]
    },
)
