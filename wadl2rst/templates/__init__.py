#!/usr/bin/env python

import os
import glob
import logging
from pkg_resources import resource_filename

import jinja2

log = logging.getLogger(__name__)


class Data(dict):
    """ Holder for the templates. """

    def __init__(self):
        self.env = jinja2.Environment(
            keep_trailing_newline=True,
        )

        glob_path = os.path.join(resource_filename('wadl2rst', 'templates'), '*.jinja')

        for file_path in glob.glob(glob_path):
            name_parts = os.path.basename(file_path).split('.')[0:-1]
            name = ".".join(name_parts)
            with open(file_path, 'r') as file:
                data = file.read().decode('ascii', 'ignore')
                self[name] = self.env.from_string(data)

# Singleton instance
templates = Data()
