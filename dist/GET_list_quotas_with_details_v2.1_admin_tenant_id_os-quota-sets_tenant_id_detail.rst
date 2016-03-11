=============================================================================
List Quotas With Details -  OpenStack Compute API v2.1
=============================================================================

List Quotas With Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_quotas_with_details_v2.1_admin_tenant_id_os-quota-sets_tenant_id_detail.rst#request>`__
`Response <GET_list_quotas_with_details_v2.1_admin_tenant_id_os-quota-sets_tenant_id_detail.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}/detail

Lists quotas with details for a project or a project and a user.

To list a quota for a project and a user, specify the ``user_id`` query parameter.



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
|{admin_tenant_id}         |csapi:UUID               |The UUID of the          |
|                          |                         |administrative tenant.   |
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
|reserved                    |xsd:int *(Required)*    |The reserved quota      |
|                            |                        |value.                  |
+----------------------------+------------------------+------------------------+
|limit                       |xsd:int *(Required)*    |The maximum limit for   |
|                            |                        |the quota.              |
+----------------------------+------------------------+------------------------+
|in_use                      |xsd:int *(Required)*    |The in-use quota value. |
+----------------------------+------------------------+------------------------+





**Example List Quotas With Details: JSON request**


.. code::

    {"quota_set": {"injected_file_content_bytes": {"reserved": 0,"limit": 10240,"in_use": 0},"metadata_items": {"reserved": 0,"limit": 128,"in_use": 0},"server_group_members": {"reserved": 0,"limit": 10,"in_use": 0},"server_groups": {"reserved": 0,"limit": 10,"in_use": 0},"ram": {"reserved": 0,"limit": 51200,"in_use": 0},"floating_ips": {"reserved": 0,"limit": 10,"in_use": 0},"key_pairs": {"reserved": 0,"limit": 120,"in_use": 0},"id": "91a3c6da787643c78f2a7c7428fa54f2","instances": {"reserved": 0,"limit": 10,"in_use": 0},"security_group_rules": {"reserved": 0,"limit": 20,"in_use": 0},"injected_files": {"reserved": 0,"limit": 5,"in_use": 0},"cores": {"reserved": 0,"limit": 20,"in_use": 0},"fixed_ips": {"reserved": 0,"limit": -1,"in_use": 0},"injected_file_path_bytes": {"reserved": 0,"limit": 255,"in_use": 0},"security_groups": {"reserved": 0,"limit": 10,"in_use": 0}}}

