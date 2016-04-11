
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







**Example Create Agent Build: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-agents/agent-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Agent Build: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-agents/agent-create-resp.json
   :language: javascript

