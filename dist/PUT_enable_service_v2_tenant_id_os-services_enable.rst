=============================================================================
Enable Service -  OpenStack Compute API v2.1
=============================================================================

Enable Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_enable_service_v2_tenant_id_os-services_enable.rst#request>`__
`Response <PUT_enable_service_v2_tenant_id_os-services_enable.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/os-services/enable

Enables a service.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|binary                    |xsd:string *(Required)*  |The name of the service  |
|                          |                         |binary that you want to  |
|                          |                         |enable. Typically, this  |
|                          |                         |name is the base name of |
|                          |                         |the executable.          |
+--------------------------+-------------------------+-------------------------+
|host                      |xsd:string *(Required)*  |The host name of the     |
|                          |                         |service that you want to |
|                          |                         |enable.                  |
+--------------------------+-------------------------+-------------------------+





**Example Enable Service: JSON request**


.. code::

    {"binary": "manila-share","host": "openstack@cmode"}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|binary                    |xsd:string *(Required)*  |The name of the enabled  |
|                          |                         |service binary.          |
|                          |                         |Typically, this name is  |
|                          |                         |the base name of the     |
|                          |                         |executable.              |
+--------------------------+-------------------------+-------------------------+
|host                      |xsd:string *(Required)*  |The host name of enabled |
|                          |                         |service.                 |
+--------------------------+-------------------------+-------------------------+
|disabled                  |xsd:bool *(Required)*    |Indicates whether the    |
|                          |                         |service is disabled.     |
+--------------------------+-------------------------+-------------------------+





**Example Enable Service: JSON request**


.. code::

    {"disabled": false,"binary": "manila-share","host": "openstack@cmode"}

