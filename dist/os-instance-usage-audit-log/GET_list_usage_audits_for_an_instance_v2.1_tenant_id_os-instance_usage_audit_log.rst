
List Usage Audits For An Instance
=================================

`Request <GET_list_usage_audits_for_an_instance_v2.1_tenant_id_os-instance_usage_audit_log.rst#request>`__
`Response <GET_list_usage_audits_for_an_instance_v2.1_tenant_id_os-instance_usage_audit_log.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-instance_usage_audit_log

Lists usage audits for an instance.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^





**Example List Usage Audits For An Instance: JSON request**


.. code::

    {
        "instance_usage_audit_logs": {
            "hosts_not_run": [
                "f4eb7cfd155f4574967f8b55a7faed75"
            ],
            "log": {},
            "num_hosts": 1,
            "num_hosts_done": 0,
            "num_hosts_not_run": 1,
            "num_hosts_running": 0,
            "overall_status": "0 of 1 hosts done. 0 errors.",
            "period_beginning": "2012-12-01 00:00:00",
            "period_ending": "2013-01-01 00:00:00",
            "total_errors": 0,
            "total_instances": 0
        }
    }
    

