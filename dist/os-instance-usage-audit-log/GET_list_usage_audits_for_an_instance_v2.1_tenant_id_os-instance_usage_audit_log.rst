
List Usage Audits For An Instance
=================================

.. rest_method:: GET /v2.1/{tenant_id}/os-instance_usage_audit_log

Lists usage audits for an instance.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listUsageAuditsForAnInstance.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^





**Example List Usage Audits For An Instance: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-instance-usage-audit-log/usage-audits-list-resp.json
   :language: javascript


