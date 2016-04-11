
Show Metadata Item Details
==========================

`Request <GET_show_metadata_item_details_v2.1_tenant_id_servers_server_id_metadata_key_.rst#request>`__
`Response <GET_show_metadata_item_details_v2.1_tenant_id_servers_server_id_metadata_key_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/metadata/{key}

Shows details for a metadata item, by key, for a server.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Metadata Item Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/metadata/server-metadata-show-resp.json
   :language: javascript

