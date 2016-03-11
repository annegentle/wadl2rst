=============================================================================
Show Cell Data -  OpenStack Compute API v2.1
=============================================================================

Show Cell Data
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_cell_data_v2.1_tenant_id_os-cells_cell_id_.rst#request>`__
`Response <GET_show_cell_data_v2.1_tenant_id_os-cells_cell_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-cells/{cell_id}

Shows data for a cell.

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
|{cell_id}                 |csapi:UUID               |The UUID of the cell.    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Cell Data: JSON request**


.. code::

    {
        "cell": {
            "name": "cell3",
            "rpc_host": null,
            "rpc_port": null,
            "type": "child",
            "username": "username3"
        }
    }
    

