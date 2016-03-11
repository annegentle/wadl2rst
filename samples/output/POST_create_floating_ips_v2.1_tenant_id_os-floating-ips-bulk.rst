=============================================================================
Create Floating Ips -  OpenStack Compute API v2.1
=============================================================================

Create Floating Ips
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_floating_ips_v2.1_tenant_id_os-floating-ips-bulk.rst#request>`__
`Response <POST_create_floating_ips_v2.1_tenant_id_os-floating-ips-bulk.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-floating-ips-bulk

Bulk-creates floating IPs.



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
|ip_range                  |xsd:string *(Required)*  |The range of IP          |
|                          |                         |addresses to use for     |
|                          |                         |creating floating IPs.   |
+--------------------------+-------------------------+-------------------------+





**Example Create Floating Ips: JSON request**


.. code::

    {
        "floating_ips_bulk_create": {
            "ip_range": "192.168.1.0/24",
            "pool": "nova",
            "interface": "eth0"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Floating Ips: JSON request**


.. code::

    {
        "floating_ips_bulk_create": {
            "interface": "eth0",
            "ip_range": "192.168.1.0/24",
            "pool": "nova"
        }
    }
    

