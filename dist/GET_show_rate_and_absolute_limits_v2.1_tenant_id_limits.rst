=============================================================================
Show Rate And Absolute Limits -  OpenStack Compute API v2.1
=============================================================================

Show Rate And Absolute Limits
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_rate_and_absolute_limits_v2.1_tenant_id_limits.rst#request>`__
`Response <GET_show_rate_and_absolute_limits_v2.1_tenant_id_limits.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/limits

Shows rate and absolute limits for the tenant.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





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
    

