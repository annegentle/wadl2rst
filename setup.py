#!/usr/bin/env python

from setuptools import setup, find_packages

# project dependencies
install_requires = [
    "Jinja2==2.7.3",
    "PyYAML==3.11"
]

# Setuptools configuration, used to create python .eggs and such.
# See: http://bashelton.com/2009/04/setuptools-tutorial/ for a nice
# setuptools tutorial.
setup(
    name="wadl2rst",
    version="0.1",

    # packaging info
    package_data={'': ['*.jinja']},
    packages=find_packages(exclude=['test', 'test.*', 'samples', 'samples.*']),

    # requirements
    install_requires=install_requires,

    entry_points={
        'console_scripts': [
            'wadl2rst = wadl2rst.main:main'
        ]
    },

    zip_safe=False
)
