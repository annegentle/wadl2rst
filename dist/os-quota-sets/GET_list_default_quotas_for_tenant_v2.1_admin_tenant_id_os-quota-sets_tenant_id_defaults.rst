
List Default Quotas For Tenant
==============================

.. rest_method:: GET /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}/defaults

Lists the default quotas for a project.

In the request URI, you specify both the ID of the administrative project and the ID of the project for which you want to show default quotas. These project IDs can match.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listDefaultQuotasForTenant.yaml

	- admin_tenant_id: admin_tenant_id
	- tenant_id: tenant_id








Response
^^^^^^^^


.. rest_parameters:: ../listDefaultQuotasForTenant.yaml

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




**Example List Default Quotas For Tenant: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-quota-sets/quotas-default-list-resp.json
   :language: javascript


