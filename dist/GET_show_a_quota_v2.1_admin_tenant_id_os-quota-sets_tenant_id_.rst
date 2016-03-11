=============================================================================
Show A Quota -  OpenStack Compute API v2.1
=============================================================================

Show A Quota
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_a_quota_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#request>`__
`Response <GET_show_a_quota_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}

Show the quota for a project or a project and a user.

In the request URI, you specify both the ID of the administrative project and the ID of the project for which you want to show quota.

To show a quota for a project and a user, specify the ``user_id`` query parameter.



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





**Example Show A Quota: JSON request**


.. code::

    {"quota_set": {"cores": 20,"fixed_ips": -1,"floating_ips": 10,"id": "fake_tenant","injected_file_content_bytes": 10240,"injected_file_path_bytes": 255,"injected_files": 5,"instances": 10,"key_pairs": 100,"metadata_items": 128,"ram": 51200,"security_group_rules": 20,"security_groups": 10,"server_groups": 10,"server_group_members": 10}}

