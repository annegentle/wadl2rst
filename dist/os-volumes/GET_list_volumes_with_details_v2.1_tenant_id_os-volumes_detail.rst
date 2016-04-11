
List Volumes With Details
=========================

`Request <GET_list_volumes_with_details_v2.1_tenant_id_os-volumes_detail.rst#request>`__
`Response <GET_list_volumes_with_details_v2.1_tenant_id_os-volumes_detail.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-volumes/detail

Lists all volumes with details.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Volumes With Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/volumes-list-detail-resp.json
   :language: javascript

