
List Cloudpipes
===============

.. rest_method:: GET /v2.1/{tenant_id}/os-cloudpipe

Lists cloudpipes.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listCloudpipes.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^





**Example List Cloudpipes: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-cloudpipe/cloud-pipe-show-resp.json
   :language: javascript


