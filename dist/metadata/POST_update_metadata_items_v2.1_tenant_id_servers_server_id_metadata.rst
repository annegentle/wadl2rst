
Update Metadata Items
=====================

`Request <POST_update_metadata_items_v2.1_tenant_id_servers_server_id_metadata.rst#request>`__
`Response <POST_update_metadata_items_v2.1_tenant_id_servers_server_id_metadata.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/metadata

Updates one or more metadata items for a server.

Replaces metadata items that match keys. Does not modify items that are not in the request.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Update Metadata Items: JSON request**


.. literalinclude:: ../../../doc/api_samples/metadata/server-metadata-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Update Metadata Items: JSON request**


.. literalinclude:: ../../../doc/api_samples/metadata/server-metadata-list-resp.json
   :language: javascript

