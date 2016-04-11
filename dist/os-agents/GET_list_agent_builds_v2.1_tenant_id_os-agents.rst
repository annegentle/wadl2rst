
List Agent Builds
=================

.. rest_method:: GET /v2.1/{tenant_id}/os-agents

Lists agent builds.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listAgentBuilds.yaml

	- tenant_id: tenant_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../listAgentBuilds.yaml

	- agent_id: agent_id
	- architecture: architecture
	- hypervisor: hypervisor
	- url: url
	- md5hash: md5hash
	- version: version




Response
^^^^^^^^





**Example List Agent Builds: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-agents/agents-list-resp.json
   :language: javascript


