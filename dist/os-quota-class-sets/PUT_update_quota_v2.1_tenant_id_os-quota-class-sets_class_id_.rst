
Update Quota
============

`Request <PUT_update_quota_v2.1_tenant_id_os-quota-class-sets_class_id_.rst#request>`__
`Response <PUT_update_quota_v2.1_tenant_id_os-quota-class-sets_class_id_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-quota-class-sets/{class_id}

Updates quota for a class.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Update Quota: JSON request**


.. code::

    {
        "quota_class_set": {
            "instances": 50,
            "cores": 50,
            "ram": 51200,
            "floating_ips": 10,
            "metadata_items": 128,
            "injected_files": 5,
            "injected_file_content_bytes": 10240,
            "injected_file_path_bytes": 255,
            "security_groups": 10,
            "security_group_rules": 20,
            "key_pairs": 100
        }
    }
    


Response
^^^^^^^^


.. rest_parameters:: updateQuota.yaml

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




**Example Update Quota: JSON request**


.. code::

    {
        "quota_class_set": {
            "cores": 50,
            "fixed_ips": -1,
            "floating_ips": 10,
            "injected_file_content_bytes": 10240,
            "injected_file_path_bytes": 255,
            "injected_files": 5,
            "instances": 50,
            "key_pairs": 100,
            "metadata_items": 128,
            "ram": 51200,
            "security_group_rules": 20,
            "security_groups": 10
        }
    }
    

