#!/usr/bin/env python

from setuptools import setup, find_packages

# project dependencies
install_requires = [
    "Jinja2==2.7.3"
]

# Setuptools configuration, used to create python .eggs and such.
# See: http://bashelton.com/2009/04/setuptools-tutorial/ for a nice
# setuptools tutorial.
setup(
    name="wadl2html",
    version="0.1",

    # packaging infos
    package_data={'': ['*.jinja']},
    packages=find_packages(exclude=['test', 'test.*', 'samples', 'samples.*']),

    # dependency infos
    install_requires=install_requires,

    entry_points={
        'console_scripts': [
            'wadl2html = wadl2html.main:main'
        ]
    },

    zip_safe=False
)
