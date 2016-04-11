
Ping An Instance
================

.. rest_method:: GET /v2.1/{tenant_id}/os-fping/{instance_id}

Run the fping utility to ping an instance and report whether it is alive.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../pingAnInstance.yaml

	- tenant_id: tenant_id
	- instance_id: instance_id








Response
^^^^^^^^





**Example Ping An Instance: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-fping/fping-instance-show-resp.json
   :language: javascript


