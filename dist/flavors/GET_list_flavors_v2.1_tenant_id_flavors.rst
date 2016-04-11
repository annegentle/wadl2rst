
List Flavors
============

.. rest_method:: GET /v2.1/{tenant_id}/flavors

Lists flavors.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listFlavors.yaml

	- tenant_id: tenant_id



Query Parameters
~~~~~~~~~~~~~~~~

.. rest_parameters:: ../listFlavors.yaml

	- minDisk: minDisk
	- minRam: minRam
	- sort_key: sort_key
	- sort_dir: sort_dir
	- limit: limit
	- marker: marker






Response
^^^^^^^^





**Example List Flavors: JSON request**


.. literalinclude:: ../../../doc/api_samples/flavors/flavors-list-resp.json
   :language: javascript


