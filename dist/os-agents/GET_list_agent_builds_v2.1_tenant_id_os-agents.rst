
List Agent Builds
=================

`Request <GET_list_agent_builds_v2.1_tenant_id_os-agents.rst#request>`__
`Response <GET_list_agent_builds_v2.1_tenant_id_os-agents.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-agents

Lists agent builds.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|agent_id                  |csapi:UUID *(Required)*  |The UUID of the agent.   |
+--------------------------+-------------------------+-------------------------+
|architecture              |xsd:string *(Required)*  |The architecture of      |
|                          |                         |agent.                   |
+--------------------------+-------------------------+-------------------------+
|hypervisor                |xsd:string *(Required)*  |The hypervisor of agent. |
+--------------------------+-------------------------+-------------------------+
|url                       |xsd:string *(Required)*  |The URL associated with  |
|                          |                         |the agent.               |
+--------------------------+-------------------------+-------------------------+
|md5hash                   |xsd:string *(Required)*  |The MD5 hash.            |
+--------------------------+-------------------------+-------------------------+
|version                   |xsd:string *(Required)*  |The version.             |
+--------------------------+-------------------------+-------------------------+





Response
^^^^^^^^





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
    

