
Update Aggregate
================

`Request <PUT_update_aggregate_v2.1_tenant_id_os-aggregates_aggregate_id_.rst#request>`__
`Response <PUT_update_aggregate_v2.1_tenant_id_os-aggregates_aggregate_id_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-aggregates/{aggregate_id}

Updates either or both the name and availability zone for an aggregate.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Update Aggregate: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-update-req.json
   :language: javascript



Response
^^^^^^^^





**Example Update Aggregate: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-update-resp.json
   :language: javascript

