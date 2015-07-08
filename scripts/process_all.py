#!/usr/bin/env python

import glob
import os
import multiprocessing
import re
import shutil
import subprocess


""" Process all of the docs we currently know about. """

git_repos = [
    "git@github.com:openstack/barbican.git",
    "git@github.com:racker/docbook-service-registry-docs.git",
    "git@github.com:racker/ele.git",
    "git@github.com:rackerlabs/clouddocs-maven-plugin-docbook.git",
    "git@github.com:rackerlabs/clouddocs-maven-plugin.git",
    "git@github.com:rackerlabs/content-header-services.git",
    "git@github.com:rackerlabs/docs-api-reference.git",
    "git@github.com:rackerlabs/docs-cloud-backup.git",
    "git@github.com:rackerlabs/docs-cloud-big-data.git",
    "git@github.com:rackerlabs/docs-cloud-block-storage.git",
    "git@github.com:rackerlabs/docs-cloud-cdn.git",
    "git@github.com:rackerlabs/docs-cloud-databases.git",
    "git@github.com:rackerlabs/docs-cloud-dns.git",
    "git@github.com:rackerlabs/docs-cloud-files.git",
    "git@github.com:rackerlabs/docs-cloud-images.git",
    "git@github.com:rackerlabs/docs-cloud-load-balancers.git",
    "git@github.com:rackerlabs/docs-cloud-metrics.git",
    "git@github.com:rackerlabs/docs-cloud-networks.git",
    "git@github.com:rackerlabs/docs-cloud-orchestration.git",
    "git@github.com:rackerlabs/docs-cloud-queues.git",
    "git@github.com:rackerlabs/docs-cloud-rackconnect.git",
    "git@github.com:rackerlabs/olink-maven-plugin.git",
    "git@github.com:rackerlabs/otter.git",
    "git@github.com:rackerlabs/standard-usage-schemas.git",
    "git@github.com:rpcdocs/dedicated-vcloud.git",
    "git@github.com:rpcdocs/rpcdocs.git",
    "git@github.com:rpcdocs/v10.git",
    "git@github.com:rpcdocs/v4.git",
    "git@github.rackspace.com:checkmate/checkmate-docs.git",
    "git@github.rackspace.com:IX/auth-1.1.git",
    "git@github.rackspace.com:IX/auth-2.0.git",
    "git@github.rackspace.com:IX/auth-3.0.git",
    "git@github.rackspace.com:IX/auth-wadls-war.git",
    "git@github.rackspace.com:IX/cloud-networks.git",
    "git@github.rackspace.com:IX/cloud-servers-1.x.git",
    "git@github.rackspace.com:IX/cloud-servers.git",
    "git@github.rackspace.com:IX/cloud-servers.git",
    "git@github.rackspace.com:IX/email-and-apps.git",
    "git@github.rackspace.com:IX/servers-wadls-war.git",
    "git@github.rackspace.com:IX/website-resources.git",
    "git@github.rackspace.com:Product-DevOps/LandingPage2.git",
    "git@github.rackspace.com:ServiceAPIContracts/billing_service_v2.git",
    "git@github.rackspace.com:ServiceAPIContracts/billing-service.git",
    "git@github.rackspace.com:ServiceAPIContracts/configuration-service.git",
    "git@github.rackspace.com:ServiceAPIContracts/incident-service.git",
    "git@github.rackspace.com:ServiceAPIContracts/offer-service.git",
    "git@github.rackspace.com:ServiceAPIContracts/promotion_service_v1.git",
]

# directories
base_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
build_dir = os.path.join(base_dir, "build")
output_dir = os.path.join(base_dir, "dist")


def clean_build_env():
    """ delete any refuse from the build and output directories. """

    if os.path.isdir(build_dir):
        shutil.rmtree(build_dir)

    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)

    os.mkdir(build_dir)
    os.mkdir(output_dir)


def clone_repo(repo):
    """ clone each of the repos into the "build" repo. """

    try:
        cmd = ["git", "clone", repo, "--depth", "1"]
        result = subprocess.check_call(cmd, cwd=build_dir)
    except Exception, e:
        print e


def get_file_list(part):
    """ get a list of wadls for processing later. """

    output = []

    for root, dirs, files in os.walk(build_dir):
        for name in files:
            if part in name:
                output.append(os.path.join(root, name))

    return output


def resolve_entities(wadl):
    """ use xmllint to resolve the xml entities in the wadl. """

    # get the name of the wadl output
    file_base = re.sub('\.wadl$', '', wadl)
    output_file = file_base + ".resolved.wadl"

    try:
        cmd = ["xmllint", "-noent", wadl]
        output = subprocess.check_output(cmd)

        with open(output_file, 'w') as f:
            f.write(output)

    except Exception, e:
        print e


def convert_to_rst(wadl):
    """ use wadl2rst to convert the resolved wadl into an rst page. """

    # get the name of the wadl output
    file_name = os.path.split(wadl)[-1]
    file_base = re.sub('\.resolved.wadl$', '', file_name)
    book_dir = os.path.join(output_dir, file_base)

    print wadl

    try:
        os.mkdir(book_dir)
        cmd = ["wadl2rst", "Book Title Placeholder", wadl, book_dir]
        subprocess.check_output(cmd)

    except Exception, e:
        print e


if __name__ == "__main__":
    # cleanup our build environment
    clean_build_env()

    # clone all the repos
    for repo in git_repos:
        clone_repo(repo)

    # do the xmllint entity resolution on all the wadls
    pool = multiprocessing.Pool(processes=4)
    pool.map(resolve_entities, get_file_list('.wadl'))
    pool.map(convert_to_rst, get_file_list('.resolved.wadl'))
    pool.close()
    pool.join()
