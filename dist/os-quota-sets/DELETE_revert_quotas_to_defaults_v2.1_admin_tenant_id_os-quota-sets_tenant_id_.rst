
Revert Quotas To Defaults
=========================

`Request <DELETE_revert_quotas_to_defaults_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#request>`__
`Response <DELETE_revert_quotas_to_defaults_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#response>`__

.. rest_method:: DELETE /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}

Reverts the quotas to default values for a project or a project and a user.

To revert quotas for a project and a user, specify the ``user_id`` query parameter.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


.. rest_parameters:: revertQuotasToDefaults.yaml

	- user_id: user_id






Response
^^^^^^^^




