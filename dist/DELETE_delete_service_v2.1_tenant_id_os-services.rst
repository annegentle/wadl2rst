=============================================================================
Delete Service -  OpenStack Compute API v2.1
=============================================================================

Delete Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_service_v2.1_tenant_id_os-services.rst#request>`__
`Response <DELETE_delete_service_v2.1_tenant_id_os-services.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-services

Deletes a service.

Specify the service by its host name and binary name.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
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
^^^^^^^^^^^^^^^^^^




