# wadl2rst

Automates the process of taking the development wadl information from the
products and turning it into html.

[DevDoc Inventory](https://docs.google.com/spreadsheets/d/1tOHqx7xkDZ755f3PNUeXljoRRgCTNm_olwyKT6PFgb4/edit#gid=103489210) -

Mockup to correlate WADL code with transformed HTML output created.

[WADL Reference](http://www.w3.org/Submission/wadl/)

## Command Line

    xmllint -noent [input file] > [output file]
    wadl2rst [input file] > [output file]

## Developer Setup

    mkvirtualenv wadl2rst
    git clone git@github.rackspace.com:Product-DevOps/wadl2rst.git
    cd wadl2rst
    python setup.py develop

## Running the Tests

    cd /path/to/wadl2rst
    workon wadl2rst
    python setup.py nosetests

## Running pyflakes & pep8

    cd /path/to/wadl2rst
    workon wadl2rst
    python setup.py flake8
