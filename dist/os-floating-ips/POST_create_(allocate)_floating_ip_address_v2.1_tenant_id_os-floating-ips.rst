=============================================================================
Create (Allocate) Floating Ip Address -  OpenStack Compute API v2.1
=============================================================================

Create (Allocate) Floating Ip Address
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_(allocate)_floating_ip_address_v2.1_tenant_id_os-floating-ips.rst#request>`__
`Response <POST_create_(allocate)_floating_ip_address_v2.1_tenant_id_os-floating-ips.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-floating-ips

Creates, or allocates, a floating IP address for the current project. By default, the floating IP address is allocated from the public pool.

If more than one floating IP address pool is available, use the ``pool`` parameter to specify from which pool to allocate the IP address.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
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
|pool                      |                         |Pool from which to       |
|                          |                         |allocate the IP address. |
|                          |                         |If you omit this         |
|                          |                         |parameter, the call      |
|                          |                         |allocates the floating   |
|                          |                         |IP address from the      |
|                          |                         |public pool. If no       |
|                          |                         |floating IP addresses    |
|                          |                         |are available, the call  |
|                          |                         |returns the ``400``      |
|                          |                         |response code with an    |
|                          |                         |informational message.   |
|                          |                         |Policy defaults enable   |
|                          |                         |only users with the      |
|                          |                         |administrative role or   |
|                          |                         |the owner of the server  |
|                          |                         |to perform this          |
|                          |                         |operation. Cloud         |
|                          |                         |providers can change     |
|                          |                         |these permissions        |
|                          |                         |through the              |
|                          |                         |``policy.json`` file.    |
+--------------------------+-------------------------+-------------------------+





**Example Create (Allocate) Floating Ip Address: JSON request**


.. code::

    {
        "pool": "public"
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create (Allocate) Floating Ip Address: JSON request**


.. code::

    {
        "floating_ip": {
            "instance_id": null,
            "ip": "172.24.4.4",
            "fixed_ip": null,
            "id": "c9c04158-3ed4-449c-953a-aa21fb47cde7",
            "pool": "public"
        }
    }
    

