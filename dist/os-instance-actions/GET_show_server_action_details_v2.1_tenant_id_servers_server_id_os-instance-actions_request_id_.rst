
Show Server Action Details
==========================

`Request <GET_show_server_action_details_v2.1_tenant_id_servers_server_id_os-instance-actions_request_id_.rst#request>`__
`Response <GET_show_server_action_details_v2.1_tenant_id_servers_server_id_os-instance-actions_request_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-instance-actions/{request_id}

Shows details for a server action.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Server Action Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-instance-actions/instance-action-show-resp.json
   :language: javascript

