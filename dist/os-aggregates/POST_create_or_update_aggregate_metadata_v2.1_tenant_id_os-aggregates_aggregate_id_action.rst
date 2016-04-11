
Create Or Update Aggregate Metadata
===================================

`Request <POST_create_or_update_aggregate_metadata_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#request>`__
`Response <POST_create_or_update_aggregate_metadata_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Creates or replaces metadata for an aggregate.

Specify the ``set_metadata`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Create Or Update Aggregate Metadata: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-metadata-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Or Update Aggregate Metadata: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-metadata-create-resp.json
   :language: javascript

