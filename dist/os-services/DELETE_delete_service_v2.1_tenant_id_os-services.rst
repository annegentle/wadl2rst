
Delete Service
==============

`Request <DELETE_delete_service_v2.1_tenant_id_os-services.rst#request>`__
`Response <DELETE_delete_service_v2.1_tenant_id_os-services.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/os-services

Deletes a service.

Specify the service by its host name and binary name.



Normal response codes: 204,404

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





**Example Delete Service: JSON request**


.. code::

    


Response
^^^^^^^^




