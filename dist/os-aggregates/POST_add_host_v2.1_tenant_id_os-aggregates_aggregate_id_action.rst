
Add Host
========

.. rest_method:: POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Adds a host to an aggregate.

Specify the ``add_host`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../addHost.yaml

	- tenant_id: tenant_id
	- aggregate_id: aggregate_id








**Example Add Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-add-host-req.json
   :language: javascript



Response
^^^^^^^^





**Example Add Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-aggregates/aggregate-add-host-resp.json
   :language: javascript


