
Resize Server
=============

`Request <POST_resize_server_v2_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_resize_server_v2_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2/{tenant_id}/servers/{server_id}/action

Resizes a server.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Resize Server: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/server-resize-create-req.json
   :language: javascript



Response
^^^^^^^^



