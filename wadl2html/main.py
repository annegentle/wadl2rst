
""" Application Entry Point """

import argparse

from wadl2html import tree
from wadl2html.transformations.resolve_internal import resolve_internal
from wadl2html.transformations.collapse_resources import collapse_resources
from wadl2html.transformations.invert_method import invert_method


def main():
    """ Application entry point.
    Collects the command line options and passes them to wadl2html for
    processing. """

    args = parse_arguments()
    print wadl2html(args.wadl_file)


def parse_arguments():
    """Parses the command line options."""

    parser = argparse.ArgumentParser(
        description="""Given a wadl, return the html representation""")

    parser.add_argument("wadl_file",
                        type=argparse.FileType('r'),
                        help="Input file to process.")

    return parser.parse_args()


def wadl2html(wadl_file):
    """Given a wadl, return the html representation."""

    # turn the xml into in intermediate representation we can use
    ir = tree.xml_file_to_tree(wadl_file)

    # collapse nested resources into just the leaf node
    collapse_resources(ir)

    # resolve the internal references in the tree
    resolve_internal(ir)

    # make the resources children of the methods
    invert_method(ir)

    # turn our ir into html
    return ir.to_html()
