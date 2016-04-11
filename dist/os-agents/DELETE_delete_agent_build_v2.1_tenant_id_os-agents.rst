
Delete Agent Build
==================

.. rest_method:: DELETE /v2.1/{tenant_id}/os-agents

Deletes an existing agent build.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteAgentBuild.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^




