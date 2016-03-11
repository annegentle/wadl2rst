=============================================================================
List Endpoint Templates -  OpenStack Compute API v2.1
=============================================================================

List Endpoint Templates
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_endpoint_templates_v2.0_os-kscatalog_endpointtemplates.rst#request>`__
`Response <GET_list_endpoint_templates_v2.0_os-kscatalog_endpointtemplates.rst#response>`__

.. code-block:: javascript

    GET /v2.0/OS-KSCATALOG/endpointTemplates

Lists endpoint templates.



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
|serviceId                 |xsd:string *(Required)*  |The service ID.          |
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





**Example List Endpoint Templates: JSON request**


.. code::

    {"OS-KSCATALOG:endpointsTemplates": [{"id": 1,"region": "North","global": true,"type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","enabled": true},{"id": 2,"region": "South","type": "compute","publicURL": "https://compute.south.public.com/v1","internalURL": "https://compute.south.internal.com/v1","enabled": false},{"id": 3,"region": "North","global": true,"type": "object-store","publicURL": "https://object-store.north.public.com/v1.0","enabled": true},{"id": 4,"region": "South","type": "object-store","publicURL": "https://object-store.south.public.com/v2","enabled": true},{"id": 5,"global": true,"type": "OS-DNS:DNS","publicURL": "https://dns.public.com/v3.2","enabled": true}],"OS-KSCATALOG:endpointsTemplates_links": []}

