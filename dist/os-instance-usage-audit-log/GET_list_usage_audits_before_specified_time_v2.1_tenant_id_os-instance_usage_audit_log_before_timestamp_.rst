
List Usage Audits Before Specified Time
=======================================

`Request <GET_list_usage_audits_before_specified_time_v2.1_tenant_id_os-instance_usage_audit_log_before_timestamp_.rst#request>`__
`Response <GET_list_usage_audits_before_specified_time_v2.1_tenant_id_os-instance_usage_audit_log_before_timestamp_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-instance_usage_audit_log/{before_timestamp}

Lists usage audits that occurred before a specified time.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


.. rest_parameters:: ../listUsageAuditsBeforeSpecifiedTime.yaml

	- before_timestamp: before_timestamp






Response
^^^^^^^^





**Example List Usage Audits Before Specified Time: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-instance-usage-audit-log/usage-audits-log-list-resp.json
   :language: javascript

