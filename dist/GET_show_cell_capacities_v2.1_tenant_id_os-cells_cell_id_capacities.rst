=============================================================================
Show Cell Capacities -  OpenStack Compute API v2.1
=============================================================================

Show Cell Capacities
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_cell_capacities_v2.1_tenant_id_os-cells_cell_id_capacities.rst#request>`__
`Response <GET_show_cell_capacities_v2.1_tenant_id_os-cells_cell_id_capacities.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-cells/{cell_id}/capacities

Shows capacities for a cell.

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





**Example Show Cell Capacities: JSON request**


.. code::

    {
        "cell": {
            "capacities": {
                "disk_free": {
                    "total_mb": 1052672,
                    "units_by_mb": {
                        "0": 0,
                        "163840": 5,
                        "20480": 46,
                        "40960": 23,
                        "81920": 11
                    }
                },
                "ram_free": {
                    "total_mb": 7680,
                    "units_by_mb": {
                        "16384": 0,
                        "2048": 3,
                        "4096": 1,
                        "512": 13,
                        "8192": 0
                    }
                }
            }
        }
    }
    

