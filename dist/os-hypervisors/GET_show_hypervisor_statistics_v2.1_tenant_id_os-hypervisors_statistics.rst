
Show Hypervisor Statistics
==========================

.. rest_method:: GET /v2.1/{tenant_id}/os-hypervisors/statistics

Shows summary statistics for all hypervisors over all compute nodes.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showHypervisorStatistics.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^





**Example Show Hypervisor Statistics: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hypervisors/hypervisor-statistics-show-resp.json
   :language: javascript


