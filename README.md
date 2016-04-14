# wadl2rst

Automates the process of taking the WADL API information and outputting it as
RST.

## Installation

    pip install -e git+git@github.com:annegentle/wadl2rst.git@master#egg=wadl2rst

## Command Line Usage

    usage: wadl2rst [-h] [--version] [config_file]

    Given a config file, generate rST based on the WADLs contained therein. If
    there is no config_file given, it will look for a file named
    'wadl2html.config.yaml' in the current working directory.

    positional arguments:
     config_file  configuration file containing information to run

    optional arguments:
     -h, --help   show this help message and exit
     --version    print the version of the application and exit

## Config file Format

File format:

    [wadl_path]:
        title: [book_title]
        output_file: [output_file]
        preamble: [preamble]

- *wadl_path*: Path to the WADL file to process, can be relative or absolute
- *book_title*: Book title as shown on the title of the RST pages
- *output_file*: Target file to put the results into. The path name can be relative or absolute
- *preamble*: Optional preamble text you want to insert into the resulting RST page.

Place the config file in a directory near where the WADL files can have their
entity references and request example inclusions properly resolved. For
example, you can clone the openstack/api-site repo and then place a
`config.yaml` file in the `api-ref/src/wadls/` directory.

File format example:

    ../api-site/api-ref/src/wadls/compute-api/src/v2.1/wadl/os-availability-zone-v2.1.wadl:
        title: OpenStack Compute API v2.1
        output_file: dist/availability_zone.inc

## Known Issues

* Currently the example info is Compute-specific.

## Developer Setup

    mkvirtualenv wadl2rst
    git clone git@github.com:annegentle/wadl2rst.git
    cd wadl2rst
    python setup.py develop
    pip install -r requirements.txt

## Running the Tests

    cd /path/to/wadl2rst
    workon wadl2rst
    python setup.py nosetests [--with-coverage]

## Running pyflakes & pep8

    cd /path/to/wadl2rst
    workon wadl2rst
    python setup.py flake8
