
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|host                      |xsd:string *(Required)*  |The host name.           |
+--------------------------+-------------------------+-------------------------+
|binary                    |xsd:string *(Required)*  |The service name.        |
+--------------------------+-------------------------+-------------------------+
|disabled_reason           |xsd:string *(Required)*  |The reason the service   |
|                          |                         |was disabled.            |
+--------------------------+-------------------------+-------------------------+





**Example Log Disabled Service Information: JSON request**


.. code::

    


Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|service                   |xsd:string *(Required)*  |A ``service`` object.    |
+--------------------------+-------------------------+-------------------------+
|binary                    |xsd:string *(Required)*  |The service name.        |
+--------------------------+-------------------------+-------------------------+
|disabled_reason           |xsd:string *(Required)*  |The reason the service   |
|                          |                         |was disabled.            |
+--------------------------+-------------------------+-------------------------+
|host                      |xsd:string *(Required)*  |The host name.           |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |The service status,      |
|                          |                         |which is ``enabled`` or  |
|                          |                         |``disabled``.            |
+--------------------------+-------------------------+-------------------------+





**Example Log Disabled Service Information: JSON request**


.. code::

    

