=============================================================================
List Endpoints -  OpenStack Compute API v2.1
=============================================================================

List Endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_endpoints_v2.0_tenants_tenantid_os-kscatalog_endpoints.rst#request>`__
`Response <GET_list_endpoints_v2.0_tenants_tenantid_os-kscatalog_endpoints.rst#response>`__

.. code-block:: javascript

    GET /v2.0/tenants/{tenantId}/OS-KSCATALOG/endpoints

Lists endpoints for a tenant.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|203                       |                         |                         |
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
|413                       |                         |                         |
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



This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|limit                     |xsd:int *(Required)*     |Requests a page size of  |
|                          |                         |items. Returns a number  |
|                          |                         |of items up to a limit   |
|                          |                         |value. Use the ``limit`` |
|                          |                         |parameter to make an     |
|                          |                         |initial limited request  |
|                          |                         |and use the ID of the    |
|                          |                         |last-seen item from the  |
|                          |                         |response as the          |
|                          |                         |``marker`` parameter     |
|                          |                         |value in a subsequent    |
|                          |                         |limited request.         |
+--------------------------+-------------------------+-------------------------+
|marker                    |xsd:string *(Required)*  |The ID of the last-seen  |
|                          |                         |item. Use the ``limit``  |
|                          |                         |parameter to make an     |
|                          |                         |initial limited request  |
|                          |                         |and use the ID of the    |
|                          |                         |last-seen item from the  |
|                          |                         |response as the          |
|                          |                         |``marker`` parameter     |
|                          |                         |value in a subsequent    |
|                          |                         |limited request.         |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^





**Example List Endpoints: JSON request**


.. code::

    {"endpoints": [{"id": 1,"tenantId": "1","region": "North","type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","adminURL": "https://compute.north.internal.com/v1"},{"id": 2,"tenantId": "1","region": "South","type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","adminURL": "https://compute.north.internal.com/v1"},{"id": 3,"tenantId": "1","region": "East","type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","adminURL": "https://compute.north.internal.com/v1"},{"id": 4,"tenantId": "1","region": "West","type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","adminURL": "https://compute.north.internal.com/v1"},{"id": 5,"tenantId": "1","region": "Global","type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","adminURL": "https://compute.north.internal.com/v1"}],"endpoints_links": []}

