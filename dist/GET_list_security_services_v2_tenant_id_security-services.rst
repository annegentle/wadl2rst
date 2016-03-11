=============================================================================
List Security Services -  OpenStack Compute API v2.1
=============================================================================

List Security Services
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_security_services_v2_tenant_id_security-services.rst#request>`__
`Response <GET_list_security_services_v2_tenant_id_security-services.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/security-services

Lists all security services.



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

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|status                    |xsd:string *(Required)*  |The security service     |
|                          |                         |status.                  |
+--------------------------+-------------------------+-------------------------+
|type                      |xsd:string *(Required)*  |The security service     |
|                          |                         |type. A valid value is   |
|                          |                         |``ldap``, ``kerberos``,  |
|                          |                         |or ``active_directory``. |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The security service ID. |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The security service     |
|                          |                         |name.                    |
+--------------------------+-------------------------+-------------------------+





**Example List Security Services: JSON request**


.. code::

    {"security_services": [{"status": "new","type": "kerberos","id": "3c829734-0679-4c17-9637-801da48c0d5f","name": "SecServ1"},{"status": "new","type": "ldap","id": "5a1d3a12-34a7-4087-8983-50e9ed03509a","name": "SecServ2"}]}

