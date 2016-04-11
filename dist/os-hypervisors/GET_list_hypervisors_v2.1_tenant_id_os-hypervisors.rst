
List Hypervisors
================

.. rest_method:: GET /v2.1/{tenant_id}/os-hypervisors

Lists hypervisors.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listHypervisors.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^





**Example List Hypervisors: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hypervisors/hypervisors-list-resp.json
   :language: javascript


