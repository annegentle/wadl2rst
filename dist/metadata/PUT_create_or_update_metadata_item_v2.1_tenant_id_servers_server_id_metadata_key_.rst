
Create Or Update Metadata Item
==============================

`Request <PUT_create_or_update_metadata_item_v2.1_tenant_id_servers_server_id_metadata_key_.rst#request>`__
`Response <PUT_create_or_update_metadata_item_v2.1_tenant_id_servers_server_id_metadata_key_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/servers/{server_id}/metadata/{key}

Creates or replaces a metadata item, by key, for a server.

Creates a metadata item that does not already exist in the server. Removes and completely replaces a metadata item that already exists in the server with the metadata item in the request.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Create Or Update Metadata Item: JSON request**


.. literalinclude:: ../../../doc/api_samples/metadata/server-metadata-item-update-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Or Update Metadata Item: JSON request**


.. literalinclude:: ../../../doc/api_samples/metadata/server-metadata-item-show-resp.json
   :language: javascript

