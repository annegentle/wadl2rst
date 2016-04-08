
List Services
=============

`Request <GET_list_services_v2.1_tenant_id_os-services.rst#request>`__
`Response <GET_list_services_v2.1_tenant_id_os-services.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-services

Lists all services for a tenant. Includes reasons, if available, for why any services were disabled.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: listServices.yaml

	- services: services
	- id: id
	- binary: binary
	- disabled_reason: disabled_reason
	- host: host
	- state: state
	- forced_down: forced_down
	- status: status
	- updated_at: updated_at
	- zone: zone




**Example List Services: JSON request**


.. code::

    

