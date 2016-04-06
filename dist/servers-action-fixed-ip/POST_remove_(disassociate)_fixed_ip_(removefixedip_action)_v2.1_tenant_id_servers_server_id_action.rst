
Remove (Disassociate) Fixed Ip (Removefixedip Action)
=====================================================

`Request <POST_remove_(disassociate)_fixed_ip_(removefixedip_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_remove_(disassociate)_fixed_ip_(removefixedip_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Removes, or disassociates, a fixed IP address from a server.

Specify the ``removeFixedIp`` action in the request body.

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
|removeFixedIp             |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Remove (Disassociate) Fixed Ip (Removefixedip Action): JSON request**


.. code::

    {
        "removeFixedIp": {
            "address": "10.0.0.4"
        }
    }
    


Response
^^^^^^^^




