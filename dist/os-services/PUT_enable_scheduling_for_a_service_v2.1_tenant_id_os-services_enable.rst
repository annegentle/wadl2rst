
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





**Example Enable Scheduling For A Service: JSON request**


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
|host                      |xsd:string *(Required)*  |The host name.           |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |The service status,      |
|                          |                         |which is ``enabled`` or  |
|                          |                         |``disabled``.            |
+--------------------------+-------------------------+-------------------------+





**Example Enable Scheduling For A Service: JSON request**


.. code::

    

