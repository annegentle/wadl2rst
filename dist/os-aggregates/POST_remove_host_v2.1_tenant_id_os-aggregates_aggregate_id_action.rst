
Remove Host
===========

`Request <POST_remove_host_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#request>`__
`Response <POST_remove_host_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Removes a host from an aggregate.

Specify the ``remove_host`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Remove Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-remove-host-req.json
   :language: javascript



Response
^^^^^^^^





**Example Remove Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-remove-host-resp.json
   :language: javascript

