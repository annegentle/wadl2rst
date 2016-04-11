
Delete Metadata Item
====================

`Request <DELETE_delete_metadata_item_v2.1_tenant_id_servers_server_id_metadata_key_.rst#request>`__
`Response <DELETE_delete_metadata_item_v2.1_tenant_id_servers_server_id_metadata_key_.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/servers/{server_id}/metadata/{key}

Deletes a metadata item, by key, from a server.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 204

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^



