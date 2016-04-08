
Lists Consoles
==============

`Request <GET_lists_consoles_v2.1_tenant_id_servers_server_id_consoles.rst#request>`__
`Response <GET_lists_consoles_v2.1_tenant_id_servers_server_id_consoles.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/consoles

Lists all consoles for a server instance.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List consoles: JSON response**


.. code::

    {
        "consoles": [
            {
                "console": {
                    "console_type": "fake",
                    "id": 1
                }
            }
        ]
    }
    

