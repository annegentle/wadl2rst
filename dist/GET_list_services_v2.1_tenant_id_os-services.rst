=============================================================================
List Services -  OpenStack Compute API v2.1
=============================================================================

List Services
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_services_v2.1_tenant_id_os-services.rst#request>`__
`Response <GET_list_services_v2.1_tenant_id_os-services.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-services

Lists all services for a tenant. Includes reasons, if available, for why any services were disabled.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


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

    

