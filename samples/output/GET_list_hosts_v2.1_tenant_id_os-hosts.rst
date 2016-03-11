=============================================================================
List Hosts -  OpenStack Compute API v2.1
=============================================================================

List Hosts
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_hosts_v2.1_tenant_id_os-hosts.rst#request>`__
`Response <GET_list_hosts_v2.1_tenant_id_os-hosts.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-hosts

Lists hosts.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Hosts: JSON request**


.. code::

    {
        "hosts": [
            {
                "host_name": "b6e4adbc193d428ea923899d07fb001e",
                "service": "conductor",
                "zone": "internal"
            },
            {
                "host_name": "09c025b0efc64211bd23fc50fa974cdf",
                "service": "compute",
                "zone": "nova"
            },
            {
                "host_name": "a942ebfa00064d9d89a9e5a175cb9ba8",
                "service": "cert",
                "zone": "internal"
            },
            {
                "host_name": "e73ec0bd35c64de4a1adfa8b8969a1f6",
                "service": "consoleauth",
                "zone": "internal"
            },
            {
                "host_name": "396a8a0a234f476eb05fb9fbc5802ba7",
                "service": "network",
                "zone": "internal"
            },
            {
                "host_name": "abffda96592c4eacaf4111c28fddee17",
                "service": "scheduler",
                "zone": "internal"
            },
            {
                "host_name": "a8820f04962a4b4ba9fe2e9540c24094",
                "service": "cells",
                "zone": "internal"
            }
        ]
    }
    

