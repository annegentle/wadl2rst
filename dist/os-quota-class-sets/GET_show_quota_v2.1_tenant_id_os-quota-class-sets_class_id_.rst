=============================================================================
Show Quota -  OpenStack Compute API v2.1
=============================================================================

Show Quota
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_quota_v2.1_tenant_id_os-quota-class-sets_class_id_.rst#request>`__
`Response <GET_show_quota_v2.1_tenant_id_os-quota-class-sets_class_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-quota-class-sets/{class_id}

Shows the quota for a class.



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
|{class_id}                |csapi:UUID               |The UUID of the quota    |
|                          |                         |class.                   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Quota: JSON request**


.. code::

    {
        "quota_class_set": {
            "cores": 20,
            "fixed_ips": -1,
            "floating_ips": 10,
            "id": "test_class",
            "injected_file_content_bytes": 10240,
            "injected_file_path_bytes": 255,
            "injected_files": 5,
            "instances": 10,
            "key_pairs": 100,
            "metadata_items": 128,
            "ram": 51200,
            "security_group_rules": 20,
            "security_groups": 10
        }
    }
    

