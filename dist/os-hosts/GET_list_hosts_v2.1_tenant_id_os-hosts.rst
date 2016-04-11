
List Hosts
==========

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts

Lists hosts.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listHosts.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^





**Example List Hosts: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/hosts-list-resp.json
   :language: javascript


