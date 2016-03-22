=============================================================================
Bulk-Delete Floating Ips -  OpenStack Compute API v2.1
=============================================================================

Bulk-Delete Floating Ips
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_bulk-delete_floating_ips_v2.1_tenant_id_os-floating-ips-bulk_delete.rst#request>`__
`Response <POST_bulk-delete_floating_ips_v2.1_tenant_id_os-floating-ips-bulk_delete.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-floating-ips-bulk/delete

Bulk-deletes floating IPs.



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
|                          |                         |addresses from which to  |
|                          |                         |bulk-delete floating IPs.|
+--------------------------+-------------------------+-------------------------+





**Example Bulk-Delete Floating Ips: JSON request**


.. code::

    {
        "ip_range": "192.168.1.0/24"
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Bulk-Delete Floating Ips: JSON request**


.. code::

    {
        "floating_ips_bulk_delete": "192.168.1.0/24"
    }
    

