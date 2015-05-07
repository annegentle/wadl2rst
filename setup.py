#!/usr/bin/env python

from setuptools import setup, find_packages

# project dependencies
install_requires = [
    "Jinja2==2.7.3",
    "pygments==2.0.2"
]

# setup and testing dependencies
setup_requires = [
    "nose==1.3.6",
    "coverage==4.0a5",
    "flake8"
]

# Setuptools configuration, used to create python .eggs and such.
# See: http://bashelton.com/2009/04/setuptools-tutorial/ for a nice
# setuptools tutorial.
setup(
    name="wadl2html",
    version="0.1",

    # packaging info
    package_data={'': ['*.jinja']},
    packages=find_packages(exclude=['test', 'test.*', 'samples', 'samples.*']),

    # requirements
    install_requires=install_requires,
    setup_requires=setup_requires,

    entry_points={
        'console_scripts': [
            'wadl2html = wadl2html.main:main'
        ]
    },

    zip_safe=False
)
