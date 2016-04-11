
Update Agent Build
==================

`Request <PUT_update_agent_build_v2.1_tenant_id_os-agents_agent_build_id_.rst#request>`__
`Response <PUT_update_agent_build_v2.1_tenant_id_os-agents_agent_build_id_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-agents/{agent_build_id}

Updates an agent build.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../updateAgentBuild.yaml

	- url: url
	- md5hash: md5hash
	- version: version




**Example Update Agent Build: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-agents/agent-update-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../updateAgentBuild.yaml

	- agent_id: agent_id
	- url: url
	- md5hash: md5hash
	- version: version




**Example Update Agent Build: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-agents/agent-update-resp.json
   :language: javascript

