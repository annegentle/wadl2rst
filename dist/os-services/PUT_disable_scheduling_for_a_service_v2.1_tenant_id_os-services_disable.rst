
Disable Scheduling For A Service
================================

`Request <PUT_disable_scheduling_for_a_service_v2.1_tenant_id_os-services_disable.rst#request>`__
`Response <PUT_disable_scheduling_for_a_service_v2.1_tenant_id_os-services_disable.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-services/disable

Disables scheduling for a service.

Specify the service by its host name and binary name.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: disableSchedulingForAService.yaml

	- host: host
	- binary: binary




**Example Disable Scheduling For A Service: JSON request**


.. code::

    


Response
^^^^^^^^


.. rest_parameters:: disableSchedulingForAService.yaml

	- service: service
	- binary: binary
	- host: host
	- status: status




**Example Disable Scheduling For A Service: JSON request**


.. code::

    

