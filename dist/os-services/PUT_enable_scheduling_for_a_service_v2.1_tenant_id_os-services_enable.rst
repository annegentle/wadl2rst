=============================================================================
Enable Scheduling For A Service -  OpenStack Compute API v2.1
=============================================================================

Enable Scheduling For A Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_enable_scheduling_for_a_service_v2.1_tenant_id_os-services_enable.rst#request>`__
`Response <PUT_enable_scheduling_for_a_service_v2.1_tenant_id_os-services_enable.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/os-services/enable

Enables scheduling for a service.

Specify the service by its host name and binary name.



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
^^^^^^^^^^^^^^^^^^


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

    

