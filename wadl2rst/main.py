
""" Application Entry Point """

import argparse
import functools
import os
import pkg_resources
import sys

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

    # get our arguments from the command line
    args = parse_arguments()

    # turn the xml into in intermediate representation we can use
    ir = tree.xml_file_to_tree(args.wadl_file)

    # execute our transfomations against the ir
    execute_translations(ir, args.wadl_file)

    # convert it into rst
    convert_ir_to_rst(ir, args.output_dir, args.title)


def parse_arguments():
    """Parses the command line options."""

    parser = argparse.ArgumentParser(
        description="""Given a wadl file, spit out an rST file for each method.""")

    parser.add_argument("--version",
                        action="store_true",
                        default=False,
                        help="print the version of the application and exit")

    parser.add_argument("title",
                        type=str,
                        help="book title",
                        nargs="?")

    parser.add_argument("wadl_file",
                        type=argparse.FileType('r'),
                        help="input file to process",
                        nargs="?")

    parser.add_argument("output_dir",
                        type=str,
                        help="destination directory",
                        nargs="?")

    args = parser.parse_args()

    if args.version:
        print_version()
        sys.exit(0)

    validate_args(args, parser)
    return args


def print_version():
    dist = pkg_resources.get_distribution("wadl2rst")
    print "wadl2rst {}".format(dist.version)


def validate_args(args, parser):

    # title, wadl_file, and output_dir are manditory, but I couldn't set them
    # so and allow for a version to be printed :(
    if (not args.output_dir) or (not args.wadl_file) or (not args.title):
        print "Error: title, wadl_file, and output_dir are all required"
        parser.print_usage()
        sys.exit(1)

    # grab the parent of the given directory
    path = os.path.abspath(args.output_dir)

    if not os.path.exists(path):
        print "Error: Output directory {} must exist.".format(path)
        parser.print_usage()
        sys.exit(1)

    if not os.path.isdir(path):
        print "Error: Output directory {} must be a directory.".format(path)
        parser.print_usage()
        sys.exit(1)

    if not os.access(path, os.W_OK):
        print "Error: Output directory {} must be writable.".format(path)
        parser.print_usage()
        sys.exit(1)


def execute_translations(ir, wadl_file):
    """Execute the translations against the IR"""

    # collapse nested resources into just the leaf node
    collapse_resources(ir)

    # resolve the internal references in the tree
    resolve_internal(ir)

    # make sure all the code elements are wrapped in samples
    wrap_code_elements(ir)

    # resolve the external code references
    path = os.path.abspath(os.path.dirname(wadl_file.name))
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

    path = os.path.abspath(output_dir)

    # get all the method nodes in the IR
    method_nodes = ir.find("method")

    for node in method_nodes:
        rst = node.to_rst(book_title)
        params = node.template_params()
        filename = node.get_filename(params, "rst")
        full_path = os.path.join(path, filename)

        print "Generating file: {}".format(full_path)

        with open(full_path, 'w') as f:
            f.write(rst.encode('utf-8', 'ignore'))
