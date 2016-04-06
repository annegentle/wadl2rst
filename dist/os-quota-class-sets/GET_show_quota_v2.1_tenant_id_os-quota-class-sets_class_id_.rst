
Show Quota
==========

`Request <GET_show_quota_v2.1_tenant_id_os-quota-class-sets_class_id_.rst#request>`__
`Response <GET_show_quota_v2.1_tenant_id_os-quota-class-sets_class_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-quota-class-sets/{class_id}

Shows the quota for a class.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- class_id: class_id







Response
^^^^^^^^


This table shows the body parameters for the response:

+----------------------------+------------------------+------------------------+
|Name                        |Type                    |Description             |
+============================+========================+========================+
|quota_set                   |xsd:dict *(Required)*   |A ``quota_set`` object. |
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
    

