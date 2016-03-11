=============================================================================
Update Security Service -  OpenStack Compute API v2.1
=============================================================================

Update Security Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_security_service_v2_tenant_id_security-services_security_service_id_.rst#request>`__
`Response <PUT_update_security_service_v2_tenant_id_security-services_security_service_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/security-services/{security_service_id}

Updates a security service.

If the security service is in ``active`` state, you can update only the ``name`` and ``description`` attributes. A security service in ``active`` state is attached to a share network with an associated share server.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|type                      |xsd:string *(Required)*  |The security service     |
|                          |                         |type. A valid value is   |
|                          |                         |``ldap``, ``kerberos``,  |
|                          |                         |or ``active_directory``. |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The security service     |
|                          |                         |name. If you specify     |
|                          |                         |this value, the name is  |
|                          |                         |updated.                 |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The security service     |
|                          |                         |description. If you      |
|                          |                         |specify this value, the  |
|                          |                         |description is updated.  |
+--------------------------+-------------------------+-------------------------+
|dns_ip                    |xsd:string *(Required)*  |The DNS IP address that  |
|                          |                         |is used inside the       |
|                          |                         |tenant network.          |
+--------------------------+-------------------------+-------------------------+
|user                      |xsd:string *(Required)*  |The security service     |
|                          |                         |user or group name that  |
|                          |                         |is used by the tenant.   |
+--------------------------+-------------------------+-------------------------+
|password                  |xsd:string *(Required)*  |The user password, if    |
|                          |                         |you specify a ``user``.  |
+--------------------------+-------------------------+-------------------------+
|domain                    |xsd:string *(Required)*  |The security service     |
|                          |                         |domain.                  |
+--------------------------+-------------------------+-------------------------+
|server                    |xsd:string *(Required)*  |The security service     |
|                          |                         |host name or IP address. |
+--------------------------+-------------------------+-------------------------+





**Example Update Security Service: JSON request**


.. code::

    {"security_service": {"domain": "my_domain","password": "***","user": "new_user","description": "Adding a description"}}


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





**Example Update Security Service: JSON request**


.. code::

    {"security_service": {"status": "new","domain": "my_domain","project_id": "16e1ab15c35a457e9c2b2aa189f544e1","name": "SecServ1","created_at": "2015-09-07T12:19:10.000000","updated_at": "2015-09-07T12:47:21.858737","server": null,"dns_ip": "10.0.0.0/24","user": "new_user","password": "pass","type": "kerberos","id": "3c829734-0679-4c17-9637-801da48c0d5f","description": "Adding a description"}}

