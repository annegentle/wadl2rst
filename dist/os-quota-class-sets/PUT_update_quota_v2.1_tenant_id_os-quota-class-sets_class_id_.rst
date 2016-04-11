
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


.. literalinclude:: ../../../doc/api_samples/os-quota-class-sets/quota-class-update-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../updateQuota.yaml

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


.. literalinclude:: ../../../doc/api_samples/os-quota-class-sets/quota-class-update-resp.json
   :language: javascript

