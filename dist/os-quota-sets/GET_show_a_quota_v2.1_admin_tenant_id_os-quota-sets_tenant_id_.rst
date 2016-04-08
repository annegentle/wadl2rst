
Show A Quota
============

`Request <GET_show_a_quota_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#request>`__
`Response <GET_show_a_quota_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#response>`__

.. rest_method:: GET /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}

Show the quota for a project or a project and a user.

In the request URI, you specify both the ID of the administrative project and the ID of the project for which you want to show quota.

To show a quota for a project and a user, specify the ``user_id`` query parameter.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: showAQuota.yaml

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




**Example Show A Quota: JSON request**


.. code::

    {
        "quota_set": {
            "cores": 20,
            "fixed_ips": -1,
            "floating_ips": 10,
            "id": "fake_tenant",
            "injected_file_content_bytes": 10240,
            "injected_file_path_bytes": 255,
            "injected_files": 5,
            "instances": 10,
            "key_pairs": 100,
            "metadata_items": 128,
            "ram": 51200,
            "security_group_rules": 20,
            "security_groups": 10,
            "server_groups": 10,
            "server_group_members": 10
        }
    }
    

