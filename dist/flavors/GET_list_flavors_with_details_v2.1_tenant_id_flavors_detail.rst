
List Flavors With Details
=========================

`Request <GET_list_flavors_with_details_v2.1_tenant_id_flavors_detail.rst#request>`__
`Response <GET_list_flavors_with_details_v2.1_tenant_id_flavors_detail.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/flavors/detail

Lists flavors with details.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


.. rest_parameters:: ../listFlavorsWithDetails.yaml

	- minDisk: minDisk
	- minRam: minRam
	- sort_key: sort_key
	- sort_dir: sort_dir
	- limit: limit
	- marker: marker






Response
^^^^^^^^





**Example List Flavors With Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/flavors/flavors-list-detail-resp.json
   :language: javascript

