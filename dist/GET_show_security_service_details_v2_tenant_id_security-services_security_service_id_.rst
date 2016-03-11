=============================================================================
Show Security Service Details -  OpenStack Compute API v2.1
=============================================================================

Show Security Service Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_security_service_details_v2_tenant_id_security-services_security_service_id_.rst#request>`__
`Response <GET_show_security_service_details_v2_tenant_id_security-services_security_service_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/security-services/{security_service_id}

Shows details for a security service.



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
|{security_service_id}     |csapi:UUID               |The UUID of the security |
|                          |                         |service.                 |
+--------------------------+-------------------------+-------------------------+
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
|status          |xsd:string     |The security service status.                 |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|id              |csapi:UUID     |The security service ID.                     |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|project_id      |csapi:UUID     |The UUID of the project where the security   |
|                |*(Required)*   |service was created.                         |
+----------------+---------------+---------------------------------------------+
|type            |xsd:string     |The security service type. A valid value is  |
|                |*(Required)*   |``ldap``, ``kerberos``, or                   |
|                |               |``active_directory``.                        |
+----------------+---------------+---------------------------------------------+
|name            |xsd:string     |The security service name.                   |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|description     |xsd:string     |The security service description.            |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|dns_ip          |xsd:string     |The DNS IP address that is used inside the   |
|                |*(Required)*   |tenant network.                              |
+----------------+---------------+---------------------------------------------+
|user            |xsd:string     |The security service user or group name that |
|                |*(Required)*   |is used by the tenant.                       |
+----------------+---------------+---------------------------------------------+
|password        |xsd:string     |The user password, if you specify a ``user``.|
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|domain          |xsd:string     |The security service domain.                 |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|server          |xsd:string     |The security service host name or IP address.|
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|created_at      |xsd:dateTime   |The date and time stamp when the security    |
|                |*(Required)*   |service was created. The date and time stamp |
|                |               |format is `ISO 8601                          |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``.                         |
+----------------+---------------+---------------------------------------------+
|updated_at      |xsd:dateTime   |The date and time stamp when the security    |
|                |*(Required)*   |service was updated. The date and time stamp |
|                |               |format is `ISO 8601                          |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``.                         |
+----------------+---------------+---------------------------------------------+





**Example Show Security Service Details: JSON request**


.. code::

    {"security_service": {"status": "new","domain": null,"project_id": "16e1ab15c35a457e9c2b2aa189f544e1","name": "SecServ1","created_at": "2015-09-07T12:19:10.000000","updated_at": null,"server": null,"dns_ip": "10.0.0.0/24","user": "demo","password": "supersecret","type": "kerberos","id": "3c829734-0679-4c17-9637-801da48c0d5f","description": "Creating my first Security Service"}}

