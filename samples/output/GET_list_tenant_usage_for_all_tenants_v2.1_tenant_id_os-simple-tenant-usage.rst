=============================================================================
List Tenant Usage For All Tenants -  OpenStack Compute API v2.1
=============================================================================

List Tenant Usage For All Tenants
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_tenant_usage_for_all_tenants_v2.1_tenant_id_os-simple-tenant-usage.rst#request>`__
`Response <GET_list_tenant_usage_for_all_tenants_v2.1_tenant_id_os-simple-tenant-usage.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-simple-tenant-usage

Lists usage information for all tenants.



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
|{tenant_id}               |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Tenant Usage For All Tenants: JSON request**


.. code::

    {
        "tenant_usages": [
            {
                "start": "2012-10-08T21:10:44.587336",
                "stop": "2012-10-08T22:10:44.587336",
                "tenant_id": "openstack",
                "total_hours": 1.0,
                "total_local_gb_usage": 1.0,
                "total_memory_mb_usage": 512.0,
                "total_vcpus_usage": 1.0
            }
        ]
    }
    

