=============================================================================
List Agent Builds -  OpenStack Compute API v2.1
=============================================================================

List Agent Builds
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_agent_builds_v2.1_tenant_id_os-agents.rst#request>`__
`Response <GET_list_agent_builds_v2.1_tenant_id_os-agents.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-agents

Lists agent builds.



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





**Example List Agent Builds: JSON request**


.. code::

    {
        "agents": [
            {
                "agent_id": 1,
                "architecture": "x86",
                "hypervisor": "hypervisor",
                "md5hash": "add6bb58e139be103324d04d82d8f545",
                "os": "os",
                "url": "http://example.com/path/to/resource",
                "version": "8.0"
            }
        ]
    }
    

