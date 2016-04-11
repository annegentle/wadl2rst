
List Aggregates
===============

.. rest_method:: GET /v2.1/{tenant_id}/os-aggregates

Lists all aggregates. Includes the ID, name, and availability zone for each aggregate.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listAggregates.yaml

	- tenant_id: tenant_id








**Example List Aggregates: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example List Aggregates: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregates-list-resp.json
   :language: javascript


