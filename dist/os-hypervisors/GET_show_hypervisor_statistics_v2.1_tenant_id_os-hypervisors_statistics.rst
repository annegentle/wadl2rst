
Show Hypervisor Statistics
==========================

`Request <GET_show_hypervisor_statistics_v2.1_tenant_id_os-hypervisors_statistics.rst#request>`__
`Response <GET_show_hypervisor_statistics_v2.1_tenant_id_os-hypervisors_statistics.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-hypervisors/statistics

Shows summary statistics for all hypervisors over all compute nodes.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Hypervisor Statistics: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hypervisors/hypervisor-statistics-show-resp.json
   :language: javascript

