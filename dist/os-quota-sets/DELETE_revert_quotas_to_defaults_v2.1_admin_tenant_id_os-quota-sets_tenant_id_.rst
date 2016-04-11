
Revert Quotas To Defaults
=========================

.. rest_method:: DELETE /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}

Reverts the quotas to default values for a project or a project and a user.

To revert quotas for a project and a user, specify the ``user_id`` query parameter.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../revertQuotasToDefaults.yaml

	- admin_tenant_id: admin_tenant_id
	- tenant_id: tenant_id



Query Parameters
~~~~~~~~~~~~~~~~

.. rest_parameters:: ../revertQuotasToDefaults.yaml

	- user_id: user_id






Response
^^^^^^^^




