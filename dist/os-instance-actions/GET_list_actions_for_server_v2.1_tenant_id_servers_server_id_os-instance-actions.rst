
List Actions For Server
=======================

`Request <GET_list_actions_for_server_v2.1_tenant_id_servers_server_id_os-instance-actions.rst#request>`__
`Response <GET_list_actions_for_server_v2.1_tenant_id_servers_server_id_os-instance-actions.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-instance-actions

Lists actions for a server.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Actions For Server: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-instance-actions/instance-actions-list-resp.json
   :language: javascript

