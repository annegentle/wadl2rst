
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







Response
^^^^^^^^


.. rest_parameters:: showQuota.yaml

	- quota_set: quota_set
	- cores: cores
	- fixed_ips: fixed_ips
	- floating_ips: floating_ips
	- id: id
	- injected_file_content_bytes: injected_file_content_bytes
	- injected_file_path_bytes: injected_file_path_bytes
	- injected_files: injected_files
	- instances: instances
	- key_pairs: key_pairs
	- metadata_items: metadata_items
	- ram: ram
	- security_group_rules: security_group_rules
	- security_groups: security_groups
	- server_groups: server_groups
	- server_group_members: server_group_members




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
    

