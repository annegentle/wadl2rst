
Reset Server State (Os-Resetstate Action)
=========================================

`Request <POST_reset_server_state_(os-resetstate_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_reset_server_state_(os-resetstate_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Resets the state of a server.

Specify the ``os-resetState`` action and the ``state`` in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-resetState             |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Reset Server State (Os-Resetstate Action): JSON request**


.. code::

    {
        "os-resetState": {
            "state": "active"
        }
    }
    


Response
^^^^^^^^




