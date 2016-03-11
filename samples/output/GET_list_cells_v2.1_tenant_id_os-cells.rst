=============================================================================
List Cells -  OpenStack Compute API v2.1
=============================================================================

List Cells
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_cells_v2.1_tenant_id_os-cells.rst#request>`__
`Response <GET_list_cells_v2.1_tenant_id_os-cells.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-cells

Lists cells.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|501                       |                         |                         |
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





**Example List Cells: JSON request**


.. code::

    {
        "cells": [
            {
                "name": "cell1",
                "rpc_host": null,
                "rpc_port": null,
                "type": "child",
                "username": "username1"
            },
            {
                "name": "cell3",
                "rpc_host": null,
                "rpc_port": null,
                "type": "child",
                "username": "username3"
            },
            {
                "name": "cell5",
                "rpc_host": null,
                "rpc_port": null,
                "type": "child",
                "username": "username5"
            },
            {
                "name": "cell2",
                "rpc_host": null,
                "rpc_port": null,
                "type": "parent",
                "username": "username2"
            },
            {
                "name": "cell4",
                "rpc_host": null,
                "rpc_port": null,
                "type": "parent",
                "username": "username4"
            }
        ]
    }
    

