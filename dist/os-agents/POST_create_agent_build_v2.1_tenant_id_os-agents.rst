
Create Agent Build
==================

.. rest_method:: POST /v2.1/{tenant_id}/os-agents

Creates an agent build.



Normal response codes: 201

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createAgentBuild.yaml

	- tenant_id: tenant_id








**Example Create Agent Build: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-agents/agent-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Agent Build: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-agents/agent-create-resp.json
   :language: javascript


