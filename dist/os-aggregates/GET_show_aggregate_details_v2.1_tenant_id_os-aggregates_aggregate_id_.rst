
Show Aggregate Details
======================

.. rest_method:: GET /v2.1/{tenant_id}/os-aggregates/{aggregate_id}

Shows details for an aggregate. Details include hosts and metadata.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showAggregateDetails.yaml

	- tenant_id: tenant_id
	- aggregate_id: aggregate_id








**Example Show Aggregate Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Show Aggregate Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-show-resp.json
   :language: javascript


