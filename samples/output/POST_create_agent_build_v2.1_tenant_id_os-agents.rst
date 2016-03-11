=============================================================================
Create Agent Build -  OpenStack Compute API v2.1
=============================================================================

Create Agent Build
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_agent_build_v2.1_tenant_id_os-agents.rst#request>`__
`Response <POST_create_agent_build_v2.1_tenant_id_os-agents.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-agents

Creates an agent build.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
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








**Example Create Agent Build: JSON request**


.. code::

    {
        "agent": {
            "hypervisor": "hypervisor",
            "os": "os",
            "architecture": "x86",
            "version": "8.0",
            "md5hash": "add6bb58e139be103324d04d82d8f545",
            "url": "http://example.com/path/to/resource"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Agent Build: JSON request**


.. code::

    {
        "agent": {
            "agent_id": 1,
            "architecture": "x86",
            "hypervisor": "hypervisor",
            "md5hash": "add6bb58e139be103324d04d82d8f545",
            "os": "os",
            "url": "http://example.com/path/to/resource",
            "version": "8.0"
        }
    }
    

