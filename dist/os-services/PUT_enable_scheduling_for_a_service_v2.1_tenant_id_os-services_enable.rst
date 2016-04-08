
Enable Scheduling For A Service
===============================

`Request <PUT_enable_scheduling_for_a_service_v2.1_tenant_id_os-services_enable.rst#request>`__
`Response <PUT_enable_scheduling_for_a_service_v2.1_tenant_id_os-services_enable.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-services/enable

Enables scheduling for a service.

Specify the service by its host name and binary name.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: enableSchedulingForAService.yaml

	- host: host
	- binary: binary




**Example Enable Scheduling For A Service: JSON request**


.. code::

    


Response
^^^^^^^^


.. rest_parameters:: enableSchedulingForAService.yaml

	- service: service
	- binary: binary
	- host: host
	- status: status




**Example Enable Scheduling For A Service: JSON request**


.. code::

    

