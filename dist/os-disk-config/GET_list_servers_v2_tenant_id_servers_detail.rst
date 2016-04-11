
List Servers
============

.. rest_method:: GET /v2/{tenant_id}/servers/detail

Lists servers with detailed config drive information.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listServers.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^


.. rest_parameters:: ../listServers.yaml

	- os-disk-config:diskConfig: os-disk-config:diskConfig




**Example List Servers: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/list-servers-detail-get.json
   :language: javascript


