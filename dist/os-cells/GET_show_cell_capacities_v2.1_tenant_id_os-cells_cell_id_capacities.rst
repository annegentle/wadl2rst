
Show Cell Capacities
====================

`Request <GET_show_cell_capacities_v2.1_tenant_id_os-cells_cell_id_capacities.rst#request>`__
`Response <GET_show_cell_capacities_v2.1_tenant_id_os-cells_cell_id_capacities.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-cells/{cell_id}/capacities

Shows capacities for a cell.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- cell_id: cell_id







Response
^^^^^^^^





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
    

