#!/usr/bin/env python

import os
import glob
import logging
from pkg_resources import resource_filename

log = logging.getLogger(__name__)


class Data(dict):
    """ Holder for the fixtures. """

    def __init__(self):
        glob_path = os.path.join(resource_filename('test', 'fixtures'),
                                 '*.wadl')

        for file_path in glob.glob(glob_path):
            name_parts = os.path.basename(file_path).split('.')[0:-1]
            name = ".".join(name_parts)
            with open(file_path, 'r') as file:
                self[name] = file.read()


# Singleton instance
fixtures = Data()
