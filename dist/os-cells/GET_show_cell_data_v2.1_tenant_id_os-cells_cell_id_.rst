
Show Cell Data
==============

`Request <GET_show_cell_data_v2.1_tenant_id_os-cells_cell_id_.rst#request>`__
`Response <GET_show_cell_data_v2.1_tenant_id_os-cells_cell_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-cells/{cell_id}

Shows data for a cell.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





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
    

