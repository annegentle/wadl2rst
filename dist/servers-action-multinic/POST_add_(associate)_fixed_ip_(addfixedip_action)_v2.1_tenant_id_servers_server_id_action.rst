
Add (Associate) Fixed Ip (Addfixedip Action)
============================================

`Request <POST_add_(associate)_fixed_ip_(addfixedip_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_add_(associate)_fixed_ip_(addfixedip_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Adds a fixed IP address to a server instance, which associates that address with the server. The fixed IP address is retrieved from the network that you specify in the request.

Specify the ``addFixedIp`` action and the network ID in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: add(Associate)FixedIp(AddfixedipAction).yaml

	- addFixedIp: addFixedIp




**Example Add (Associate) Fixed Ip (Addfixedip Action): JSON request**


.. code::

    


Response
^^^^^^^^




