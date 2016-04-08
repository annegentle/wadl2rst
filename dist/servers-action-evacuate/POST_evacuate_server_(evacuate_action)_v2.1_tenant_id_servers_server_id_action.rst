
Evacuate Server (Evacuate Action)
=================================

`Request <POST_evacuate_server_(evacuate_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_evacuate_server_(evacuate_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Evacuates a server from a failed host to a new one.

Specify the ``evacuate`` action in the request body.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: evacuateServer(EvacuateAction).yaml

	- evacuate: evacuate
	- host: host
	- adminPass: adminPass




**Example Evacuate Server (Evacuate Action): JSON request**


.. code::

    {
        "evacuate": {
            "host": "b419863b7d814906a68fb31703c0dbd6",
            "adminPass": "MySecretPass"
        }
    }
    


Response
^^^^^^^^





**Example Evacuate Server (Evacuate Action): JSON request**


.. code::

    {
        "adminPass": "MySecretPass"
    }
    

