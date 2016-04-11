
Clear Admin Password
====================

.. rest_method:: DELETE /v2.1/{tenant_id}/servers/{server_id}/os-server-password

Clears the encrypted administrative password for a server, which removes it from the metadata server.

This action does not actually change the instance server password.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 204

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../clearAdminPassword.yaml

	- tenant_id: tenant_id
	- server_id: server_id








Response
^^^^^^^^




