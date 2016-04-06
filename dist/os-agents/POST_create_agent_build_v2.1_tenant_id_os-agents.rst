
Create Agent Build
==================

`Request <POST_create_agent_build_v2.1_tenant_id_os-agents.rst#request>`__
`Response <POST_create_agent_build_v2.1_tenant_id_os-agents.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-agents

Creates an agent build.



Normal response codes: 201

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







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
^^^^^^^^





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
    

