=============================================================================
Create Endpoint -  OpenStack Compute API v2.1
=============================================================================

Create Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_endpoint_v2.0_tenants_tenantid_os-kscatalog_endpoints.rst#request>`__
`Response <POST_create_endpoint_v2.0_tenants_tenantid_os-kscatalog_endpoints.rst#response>`__

.. code-block:: javascript

    POST /v2.0/tenants/{tenantId}/OS-KSCATALOG/endpoints

Creates endpoint to a tenant.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|413                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|415                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |capi:UUID                |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|X-Auth-Token              |xsd:string *(Required)*  |A valid authentication   |
|                          |                         |token for an             |
|                          |                         |administrative user.     |
+--------------------------+-------------------------+-------------------------+








**Example Create Endpoint: JSON request**


.. code::

    {"OS-KSCATALOG:endpointTemplate": {"id": 1}}


Response
^^^^^^^^^^^^^^^^^^





**Example Create Endpoint: JSON request**


.. code::

    {"endpoint": {"id": 1,"tenantId": 1,"region": "North","type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","adminURL": "https://compute.north.internal.com/v1"}}

