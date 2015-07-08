
""" Application Entry Point """

import argparse
import functools
import os
import pkg_resources
import subprocess
import sys
import tempfile

import yaml

from wadl2rst import tree
from wadl2rst.transformations.cleanup_application_node import cleanup_application_node
from wadl2rst.transformations.collapse_resources import collapse_resources
from wadl2rst.transformations.invert_method import invert_method
from wadl2rst.transformations.resolve_external_code import resolve_external_code
from wadl2rst.transformations.resolve_internal import resolve_internal
from wadl2rst.transformations.wrap_code_elements import wrap_code_elements
from wadl2rst.transformations.wrap_param_elements import wrap_param_elements
from wadl2rst.transformations.wrap_response_elements import wrap_response_elements


def main():
    """ Application entry point.
    Collects the command line options and passes them to wadl2rst for
    processing. """

    # get our config file from the arguments
    config_file = parse_arguments()
    config = yaml.load(file(config_file, 'r'))

    # for each wadl_file in the options
    for filename, options in config.items():
        # resolve the entities in the wadl docs
        proc = subprocess.Popen(
            ['xmllint', '-noent', filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output, err = proc.communicate()

        # if the returncode from this is bad, throw an error
        if proc.returncode != 0:
            print err
            sys.exit(1)

        # parse the xml file
        ir = tree.xml_string_to_tree(output)
        execute_translations(ir, filename)
        convert_ir_to_rst(ir, options['output_directory'], options['title'])


def parse_arguments():
    """Parses the command line options."""

    parser = argparse.ArgumentParser(
        description="""Given a config file, generate rST based on the WADLs contained therein.
        If there is no config_file given, it will look for a file named 'wadl2html.config.yaml'
        in the current working directory.""")

    parser.add_argument("--version",
                        action="store_true",
                        default=False,
                        help="print the version of the application and exit")

    parser.add_argument("config_file",
                        type=str,
                        help="configuration file containing information to run",
                        nargs="?")

    args = parser.parse_args()

    if args.version:
        print_version()

    if not args.config_file:
        config_file = find_config_file()
    else:
        config_file = args.config_file

    return config_file


def print_version():
    dist = pkg_resources.get_distribution("wadl2rst")
    print "wadl2rst {}".format(dist.version)
    sys.exit(0)


def find_config_file():
    config_path = os.path.join(os.getcwd(), "wadl2rst.config.yaml")

    if not os.path.isfile(config_path):
        print "Error: no file named wadl2rst.config.yaml in current directory"
        sys.exit(1)

    return config_path


def execute_translations(ir, filename):
    """Execute the translations against the IR"""

    # collapse nested resources into just the leaf node
    collapse_resources(ir)

    # resolve the internal references in the tree
    resolve_internal(ir)

    # make sure all the code elements are wrapped in samples
    wrap_code_elements(ir)

    # resolve the external code references
    path = os.path.abspath(os.path.dirname(filename))
    resolve_external_code(path, ir)

    # make the resources children of the methods
    invert_method(ir)

    # make sure the param nodes have good parents
    wrap_param_elements(ir)

    # make sure the response nodes have good parents
    wrap_response_elements(ir)

    # remove any resource type nodes
    cleanup_application_node(ir)


def convert_ir_to_rst(ir, output_dir, book_title):
    """Create an rst file in the output_dir for each method node in the IR."""

    # grab the path of the output directory, creating it if necessary
    path = os.path.abspath(output_dir)
    if not os.path.exists(path):
        print "Error: Output directory: {} does not exist!".format(path)
        sys.exit(1)

    # get all the method nodes in the IR
    method_nodes = ir.find("method")

    for node in method_nodes:
        rst = node.to_rst(book_title)

        if rst == "":
            continue

        params = node.template_params()
        filename = node.get_filename(params, "rst")
        full_path = os.path.join(path, filename)

        print "Generating file: {}".format(full_path)

        with open(full_path, 'w') as f:
            f.write(rst.encode('utf-8', 'ignore'))
