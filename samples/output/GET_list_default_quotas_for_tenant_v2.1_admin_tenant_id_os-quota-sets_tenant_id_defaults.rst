=============================================================================
List Default Quotas For Tenant -  OpenStack Compute API v2.1
=============================================================================

List Default Quotas For Tenant
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_default_quotas_for_tenant_v2.1_admin_tenant_id_os-quota-sets_tenant_id_defaults.rst#request>`__
`Response <GET_list_default_quotas_for_tenant_v2.1_admin_tenant_id_os-quota-sets_tenant_id_defaults.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}/defaults

Lists the default quotas for a project.

In the request URI, you specify both the ID of the administrative project and the ID of the project for which you want to show default quotas. These project IDs can match.



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
|{admin_tenant_id}         |csapi:UUID               |The UUID of the          |
|                          |                         |administrative tenant.   |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------------------+------------------------+------------------------+
|Name                        |Type                    |Description             |
+============================+========================+========================+
|quota_set                   |xsd:string *(Required)* |A ``quota_set`` object. |
+----------------------------+------------------------+------------------------+
|cores                       |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |instance cores for each |
|                            |                        |tenant.                 |
+----------------------------+------------------------+------------------------+
|fixed_ips                   |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |fixed IP addresses for  |
|                            |                        |each tenant. Must be    |
|                            |                        |equal to or greater     |
|                            |                        |than the number of      |
|                            |                        |allowed instances.      |
+----------------------------+------------------------+------------------------+
|floating_ips                |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |floating IP addresses   |
|                            |                        |for each tenant.        |
+----------------------------+------------------------+------------------------+
|id                          |csapi:UUID *(Required)* |The ID of the quota set.|
+----------------------------+------------------------+------------------------+
|injected_file_content_bytes |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |bytes of content for    |
|                            |                        |each injected file.     |
+----------------------------+------------------------+------------------------+
|injected_file_path_bytes    |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |bytes for each injected |
|                            |                        |file path.              |
+----------------------------+------------------------+------------------------+
|injected_files              |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |injected files for each |
|                            |                        |tenant.                 |
+----------------------------+------------------------+------------------------+
|instances                   |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |instances for each      |
|                            |                        |tenant.                 |
+----------------------------+------------------------+------------------------+
|key_pairs                   |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |key pairs for each user.|
+----------------------------+------------------------+------------------------+
|metadata_items              |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |metadata items for each |
|                            |                        |instance.               |
+----------------------------+------------------------+------------------------+
|ram                         |xsd:int *(Required)*    |The amount of allowed   |
|                            |                        |instance RAM, in MB,    |
|                            |                        |for each tenant.        |
+----------------------------+------------------------+------------------------+
|security_group_rules        |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |rules for each security |
|                            |                        |group.                  |
+----------------------------+------------------------+------------------------+
|security_groups             |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |security groups for     |
|                            |                        |each tenant.            |
+----------------------------+------------------------+------------------------+
|server_groups               |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |server groups for each  |
|                            |                        |tenant.                 |
+----------------------------+------------------------+------------------------+
|server_group_members        |xsd:int *(Required)*    |The number of allowed   |
|                            |                        |members for each server |
|                            |                        |group.                  |
+----------------------------+------------------------+------------------------+





**Example List Default Quotas For Tenant: JSON request**


.. code::

    {
        "quota_set": {
            "injected_file_content_bytes": 10240,
            "metadata_items": 128,
            "server_group_members": 10,
            "server_groups": 10,
            "ram": 51200,
            "floating_ips": 10,
            "key_pairs": 100,
            "id": "91a3c6da787643c78f2a7c7428fa54f2",
            "instances": 10,
            "security_group_rules": 20,
            "injected_files": 5,
            "cores": 20,
            "fixed_ips": -1,
            "injected_file_path_bytes": 255,
            "security_groups": 10
        }
    }
    

