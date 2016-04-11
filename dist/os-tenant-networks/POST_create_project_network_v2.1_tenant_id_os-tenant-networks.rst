
Create Project Network
======================

`Request <POST_create_project_network_v2.1_tenant_id_os-tenant-networks.rst#request>`__
`Response <POST_create_project_network_v2.1_tenant_id_os-tenant-networks.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-tenant-networks

Creates a project network.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Create Project Network: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-tenant-networks/network-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Project Network: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-tenant-networks/network-create-resp.json
   :language: javascript

