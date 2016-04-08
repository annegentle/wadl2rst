
Log Disabled Service Information
================================

`Request <PUT_log_disabled_service_information_v2.1_tenant_id_os-services_disable-log-reason.rst#request>`__
`Response <PUT_log_disabled_service_information_v2.1_tenant_id_os-services_disable-log-reason.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-services/disable-log-reason

Logs information to the service table about why a service was disabled.

Specify the service by its host name and binary name.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: logDisabledServiceInformation.yaml

	- host: host
	- binary: binary
	- disabled_reason: disabled_reason




**Example Log Disabled Service Information: JSON request**


.. code::

    


Response
^^^^^^^^


.. rest_parameters:: logDisabledServiceInformation.yaml

	- service: service
	- binary: binary
	- disabled_reason: disabled_reason
	- host: host
	- status: status




**Example Log Disabled Service Information: JSON request**


.. code::

    

