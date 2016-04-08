
Update Quotas
=============

`Request <PUT_update_quotas_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#request>`__
`Response <PUT_update_quotas_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#response>`__

.. rest_method:: PUT /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}

Update the quotas for a project or a project and a user.

You can force the update even if the quota has already been used and the reserved quota exceeds the new quota.

To force the update, specify the ``"force": "True"`` attribute in the request body. Default is ``false``. The following example request shows the optional ``force`` attribute.

To update a quota for a project and a user, specify the ``user_id`` query parameter.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


.. rest_parameters:: updateQuotas.yaml

	- user_id: user_id



.. rest_parameters:: updateQuotas.yaml

	- quota_set: quota_set
	- force: force
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




**Example Update Quotas: JSON request**


.. code::

    {
        "quota_set": {
            "force": true,
            "key_pairs": 120
        }
    }
    


Response
^^^^^^^^


.. rest_parameters:: updateQuotas.yaml

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




**Example Update Quotas: JSON request**


.. code::

    {
        "quota_set": {
            "injected_file_content_bytes": 10240,
            "metadata_items": 128,
            "server_group_members": 10,
            "server_groups": 10,
            "ram": 51200,
            "floating_ips": 10,
            "key_pairs": 120,
            "instances": 10,
            "security_group_rules": 20,
            "injected_files": 5,
            "cores": 20,
            "fixed_ips": -1,
            "injected_file_path_bytes": 255,
            "security_groups": 10
        }
    }
    

