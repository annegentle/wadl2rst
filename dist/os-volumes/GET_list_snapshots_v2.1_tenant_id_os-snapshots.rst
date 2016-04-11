
List Snapshots
==============

`Request <GET_list_snapshots_v2.1_tenant_id_os-snapshots.rst#request>`__
`Response <GET_list_snapshots_v2.1_tenant_id_os-snapshots.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-snapshots

Lists snapshots.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Snapshots: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/snapshots-list-resp.json
   :language: javascript

