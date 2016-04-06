
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^


This table shows the body parameters for the response:

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|services        |xsd:string     |A ``services`` object.                       |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|id              |csapi:UUID     |The UUID of the service.                     |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|binary          |xsd:string     |The service name.                            |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|disabled_reason |xsd:string     |The reason the service was disabled.         |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|host            |xsd:string     |The host name.                               |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|state           |xsd:string     |The service state, which is ``up`` or        |
|                |*(Required)*   |``down``.                                    |
+----------------+---------------+---------------------------------------------+
|forced_down     |xsd:string     |If you force-down the service, this value is |
|                |*(Required)*   |``true``.                                    |
+----------------+---------------+---------------------------------------------+
|status          |xsd:string     |The service status, which is ``enabled`` or  |
|                |*(Required)*   |``disabled``.                                |
+----------------+---------------+---------------------------------------------+
|updated_at      |xsd:dateTime   |The date and time when the service was       |
|                |*(Required)*   |updated. The date and time stamp format is   |
|                |               |`ISO 8601                                    |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                |               |``2015-08-27T09:49:58-05:00``. The           |
|                |               |``±hh:mm`` value, if included, is the time   |
|                |               |zone as an offset from UTC. In the previous  |
|                |               |example, the offset value is ``-05:00``. If  |
|                |               |the ``updated_at`` date and time stamp is    |
|                |               |not set, its value is ``null``.              |
+----------------+---------------+---------------------------------------------+
|zone            |xsd:string     |The availability zone of the host.           |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+





**Example List Services: JSON request**


.. code::

    

