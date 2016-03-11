=============================================================================
List Services -  OpenStack Compute API v2.1
=============================================================================

List Services
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_services_v2_tenant_id_os-services.rst#request>`__
`Response <GET_list_services_v2_tenant_id_os-services.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/os-services

Lists all services.



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
|X-Openstack-Manila-Api-   |xsd:string               |The HTTP header to       |
|Version                   |                         |specify a valid Shared   |
|                          |                         |File Systems API micro-  |
|                          |                         |version. For example,    |
|                          |                         |``"X-Openstack-Manila-   |
|                          |                         |Api-Version: 2.6"``. If  |
|                          |                         |you omit this header,    |
|                          |                         |the default micro-       |
|                          |                         |version is 2.0.          |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|id              |xsd:int        |The service ID.                              |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|status          |xsd:string     |The service status, which is ``enabled`` or  |
|                |*(Required)*   |``disabled``.                                |
+----------------+---------------+---------------------------------------------+
|binary          |xsd:string     |The service binary name. Default is the base |
|                |*(Required)*   |name of the executable.                      |
+----------------+---------------+---------------------------------------------+
|zone            |xsd:string     |The availability zone.                       |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|host            |xsd:string     |The host name.                               |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|state           |xsd:string     |The current state of the service. A valid    |
|                |*(Required)*   |value is ``up`` or ``down``.                 |
+----------------+---------------+---------------------------------------------+
|updated_at      |xsd:dateTime   |The date and time stamp when the service was |
|                |*(Required)*   |updated. The date and time stamp format is   |
|                |               |`ISO 8601                                    |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``.                         |
+----------------+---------------+---------------------------------------------+





**Example List Services: JSON request**


.. code::

    {"services": [{"status": "enabled","binary": "manila-share","zone": "nova","host": "manila2@generic1","updated_at": "2015-09-07T13:03:57.000000","state": "up","id": 1},{"status": "enabled","binary": "manila-scheduler","zone": "nova","host": "manila2","updated_at": "2015-09-07T13:03:57.000000","state": "up","id": 2}]}

