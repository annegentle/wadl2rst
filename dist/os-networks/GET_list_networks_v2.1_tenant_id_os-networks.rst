
List Networks
=============

`Request <GET_list_networks_v2.1_tenant_id_os-networks.rst#request>`__
`Response <GET_list_networks_v2.1_tenant_id_os-networks.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-networks

Lists networks for the project.

Policy defaults enable all users to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Networks: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-networks/networks-list-resp.json
   :language: javascript

