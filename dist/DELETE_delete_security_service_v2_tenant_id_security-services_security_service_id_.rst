=============================================================================
Delete Security Service -  OpenStack Compute API v2.1
=============================================================================

Delete Security Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_security_service_v2_tenant_id_security-services_security_service_id_.rst#request>`__
`Response <DELETE_delete_security_service_v2_tenant_id_security-services_security_service_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/security-services/{security_service_id}

Deletes a security service.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
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




