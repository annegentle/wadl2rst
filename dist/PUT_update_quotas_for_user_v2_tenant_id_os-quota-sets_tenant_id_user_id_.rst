=============================================================================
Update Quotas For User -  OpenStack Compute API v2.1
=============================================================================

Update Quotas For User
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_quotas_for_user_v2_tenant_id_os-quota-sets_tenant_id_user_id_.rst#request>`__
`Response <PUT_update_quotas_for_user_v2_tenant_id_os-quota-sets_tenant_id_user_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/os-quota-sets/{tenant_id}/{user_id}

Updates quotas for a tenant and user.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Update quotas for user   |                         |
|                          |response: JSON           |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{user_id}                 |xsd:string *(Required)*  |The user ID. Specify in  |
|                          |                         |the URI as               |
|                          |                         |``user_id={user_id}``.   |
+--------------------------+-------------------------+-------------------------+
|{admin_tenant_id}         |csapi:UUID               |The UUID of the          |
|                          |                         |administrative tenant.   |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+----------------------------+------------------------+------------------------+
|Name                        |Type                    |Description             |
+============================+========================+========================+
|quota_set                   |xsd:dict *(Required)*   |A ``quota_set`` object. |
+----------------------------+------------------------+------------------------+
|cores                       |xsd:int *(Required)*    |The number of instance  |
|                            |                        |cores that are allowed  |
|                            |                        |for each tenant.        |
+----------------------------+------------------------+------------------------+
|fixed_ips                   |xsd:int *(Required)*    |The number of fixed IP  |
|                            |                        |addresses that are      |
|                            |                        |allowed for each        |
|                            |                        |tenant. Must be equal   |
|                            |                        |to or greater than the  |
|                            |                        |number of allowed       |
|                            |                        |instances.              |
+----------------------------+------------------------+------------------------+
|floating_ips                |xsd:int *(Required)*    |The number of floating  |
|                            |                        |IP addresses that are   |
|                            |                        |allowed for each tenant.|
+----------------------------+------------------------+------------------------+
|id                          |xsd:int *(Required)*    |The ID for the quota    |
|                            |                        |set.                    |
+----------------------------+------------------------+------------------------+
|injected_file_content_bytes |xsd:int *(Required)*    |The number of bytes of  |
|                            |                        |content that are        |
|                            |                        |allowed for each        |
|                            |                        |injected file.          |
+----------------------------+------------------------+------------------------+
|injected_file_path_bytes    |xsd:int *(Required)*    |The number of bytes     |
|                            |                        |that are allowed for    |
|                            |                        |each injected file path.|
+----------------------------+------------------------+------------------------+
|injected_files              |xsd:int *(Required)*    |The number of injected  |
|                            |                        |files that are allowed  |
|                            |                        |for each tenant.        |
+----------------------------+------------------------+------------------------+
|instances                   |xsd:int *(Required)*    |The number of instances |
|                            |                        |that are allowed for    |
|                            |                        |each tenant.            |
+----------------------------+------------------------+------------------------+
|key_pairs                   |xsd:int *(Required)*    |The number of key pairs |
|                            |                        |that are allowed for    |
|                            |                        |each user.              |
+----------------------------+------------------------+------------------------+
|metadata_items              |xsd:int *(Required)*    |The number of metadata  |
|                            |                        |items that are allowed  |
|                            |                        |for each instance.      |
+----------------------------+------------------------+------------------------+
|ram                         |xsd:int *(Required)*    |The amount of instance  |
|                            |                        |RAM in megabytes that   |
|                            |                        |are allowed for each    |
|                            |                        |tenant.                 |
+----------------------------+------------------------+------------------------+
|security_group_rules        |xsd:int *(Required)*    |The number of rules     |
|                            |                        |that are allowed for    |
|                            |                        |each security group.    |
+----------------------------+------------------------+------------------------+
|security_groups             |xsd:int *(Required)*    |The number of security  |
|                            |                        |groups that are allowed |
|                            |                        |for each tenant.        |
+----------------------------+------------------------+------------------------+
|in_use                      |xsd:string *(Required)* |The in use data size.   |
|                            |                        |Visible only if you set |
|                            |                        |the ``usage=True``      |
|                            |                        |query parameter.        |
+----------------------------+------------------------+------------------------+
|reserved                    |xsd:int *(Required)*    |Reserved volume size.   |
|                            |                        |Visible only if you set |
|                            |                        |the ``usage=True``      |
|                            |                        |query parameter.        |
+----------------------------+------------------------+------------------------+





**Example Update quotas for user request: JSON**


.. code::

    {"quota_set": {"snapshots": 45}}


**Example Update quotas for user request: XML**


.. code::

    <?xml version='1.0' encoding='UTF-8'?><quota_set id="fake_tenant"><snapshots>45</snapshots></quota_set>


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------------------+------------------------+------------------------+
|Name                        |Type                    |Description             |
+============================+========================+========================+
|quota_set                   |xsd:dict *(Required)*   |A ``quota_set`` object. |
+----------------------------+------------------------+------------------------+
|cores                       |xsd:int *(Required)*    |The number of instance  |
|                            |                        |cores that are allowed  |
|                            |                        |for each tenant.        |
+----------------------------+------------------------+------------------------+
|fixed_ips                   |xsd:int *(Required)*    |The number of fixed IP  |
|                            |                        |addresses that are      |
|                            |                        |allowed for each        |
|                            |                        |tenant. Must be equal   |
|                            |                        |to or greater than the  |
|                            |                        |number of allowed       |
|                            |                        |instances.              |
+----------------------------+------------------------+------------------------+
|floating_ips                |xsd:int *(Required)*    |The number of floating  |
|                            |                        |IP addresses that are   |
|                            |                        |allowed for each tenant.|
+----------------------------+------------------------+------------------------+
|id                          |xsd:int *(Required)*    |The ID for the quota    |
|                            |                        |set.                    |
+----------------------------+------------------------+------------------------+
|injected_file_content_bytes |xsd:int *(Required)*    |The number of bytes of  |
|                            |                        |content that are        |
|                            |                        |allowed for each        |
|                            |                        |injected file.          |
+----------------------------+------------------------+------------------------+
|injected_file_path_bytes    |xsd:int *(Required)*    |The number of bytes     |
|                            |                        |that are allowed for    |
|                            |                        |each injected file path.|
+----------------------------+------------------------+------------------------+
|injected_files              |xsd:int *(Required)*    |The number of injected  |
|                            |                        |files that are allowed  |
|                            |                        |for each tenant.        |
+----------------------------+------------------------+------------------------+
|instances                   |xsd:int *(Required)*    |The number of instances |
|                            |                        |that are allowed for    |
|                            |                        |each tenant.            |
+----------------------------+------------------------+------------------------+
|key_pairs                   |xsd:int *(Required)*    |The number of key pairs |
|                            |                        |that are allowed for    |
|                            |                        |each user.              |
+----------------------------+------------------------+------------------------+
|metadata_items              |xsd:int *(Required)*    |The number of metadata  |
|                            |                        |items that are allowed  |
|                            |                        |for each instance.      |
+----------------------------+------------------------+------------------------+
|ram                         |xsd:int *(Required)*    |The amount of instance  |
|                            |                        |RAM in megabytes that   |
|                            |                        |are allowed for each    |
|                            |                        |tenant.                 |
+----------------------------+------------------------+------------------------+
|security_group_rules        |xsd:int *(Required)*    |The number of rules     |
|                            |                        |that are allowed for    |
|                            |                        |each security group.    |
+----------------------------+------------------------+------------------------+
|security_groups             |xsd:int *(Required)*    |The number of security  |
|                            |                        |groups that are allowed |
|                            |                        |for each tenant.        |
+----------------------------+------------------------+------------------------+
|in_use                      |xsd:string *(Required)* |The in use data size.   |
|                            |                        |Visible only if you set |
|                            |                        |the ``usage=True``      |
|                            |                        |query parameter.        |
+----------------------------+------------------------+------------------------+
|reserved                    |xsd:int *(Required)*    |Reserved volume size.   |
|                            |                        |Visible only if you set |
|                            |                        |the ``usage=True``      |
|                            |                        |query parameter.        |
+----------------------------+------------------------+------------------------+





**Example Update quotas for user response: JSON**


.. code::

    {"quota_set": {"snapshots": 45}}


**Example Show quotas for user response: XML**


.. code::

    <?xml version='1.0' encoding='UTF-8'?><quota_set id="fake_tenant"><gigabytes>5</gigabytes><snapshots>10</snapshots><volumes>20</volumes></quota_set>

