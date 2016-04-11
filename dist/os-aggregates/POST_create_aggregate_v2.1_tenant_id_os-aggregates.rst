
Create Aggregate
================

.. rest_method:: POST /v2.1/{tenant_id}/os-aggregates

Creates an aggregate in an availability zone.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createAggregate.yaml

	- tenant_id: tenant_id








**Example Create Aggregate: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Aggregate: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-create-resp.json
   :language: javascript


