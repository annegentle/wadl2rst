
Show Rate And Absolute Limits
=============================

`Request <GET_show_rate_and_absolute_limits_v2.1_tenant_id_limits.rst#request>`__
`Response <GET_show_rate_and_absolute_limits_v2.1_tenant_id_limits.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/limits

Shows rate and absolute limits for the tenant.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^





**Example Show Rate And Absolute Limits: JSON request**


.. code::

    {
        "limits": {
            "rate": [],
            "absolute": {
                "maxServerMeta": 128,
                "maxPersonality": 5,
                "totalServerGroupsUsed": 0,
                "maxImageMeta": 128,
                "maxPersonalitySize": 10240,
                "maxTotalKeypairs": 100,
                "maxSecurityGroupRules": 20,
                "maxServerGroups": 10,
                "totalCoresUsed": 1,
                "totalRAMUsed": 2048,
                "totalInstancesUsed": 1,
                "maxSecurityGroups": 10,
                "totalFloatingIpsUsed": 0,
                "maxTotalCores": 20,
                "maxServerGroupMembers": 10,
                "maxTotalFloatingIps": 10,
                "totalSecurityGroupsUsed": 1,
                "maxTotalInstances": 10,
                "maxTotalRAMSize": 51200
            }
        }
    }
    

