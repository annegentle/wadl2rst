=============================================================================
Disable Service -  OpenStack Compute API v2.1
=============================================================================

Disable Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_disable_service_v2_tenant_id_os-services_disable.rst#request>`__
`Response <PUT_disable_service_v2_tenant_id_os-services_disable.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/os-services/disable

Disables a service.



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
|                          |                         |disable. Typically, this |
|                          |                         |name is the base name of |
|                          |                         |the executable.          |
+--------------------------+-------------------------+-------------------------+
|host                      |xsd:string *(Required)*  |The host name of the     |
|                          |                         |service that you want to |
|                          |                         |disable.                 |
+--------------------------+-------------------------+-------------------------+





**Example Disable Service: JSON request**


.. code::

    {"binary": "manila-share","host": "openstack@cmode"}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|binary                    |xsd:string *(Required)*  |The name of the disabled |
|                          |                         |service binary.          |
|                          |                         |Typically, this name is  |
|                          |                         |the base name of the     |
|                          |                         |executable.              |
+--------------------------+-------------------------+-------------------------+
|host                      |xsd:string *(Required)*  |The host name of         |
|                          |                         |disabled service.        |
+--------------------------+-------------------------+-------------------------+
|disabled                  |xsd:bool *(Required)*    |Indicates whether the    |
|                          |                         |service is disabled.     |
+--------------------------+-------------------------+-------------------------+





**Example Disable Service: JSON request**


.. code::

    {"disabled": true,"binary": "manila-share","host": "openstack@cmode"}

