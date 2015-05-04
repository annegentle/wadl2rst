
""" Application Entry Point """

import argparse

from wadl2html import parser


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

    tree = parser.parse_wadl(wadl_file)
    return tree.to_html()


def main():
    """ Application entry point.
    Collects the command line options and passes them to wadl2html for
    processing. """

    args = parse_arguments()
    print wadl2html(args.wadl_file)
