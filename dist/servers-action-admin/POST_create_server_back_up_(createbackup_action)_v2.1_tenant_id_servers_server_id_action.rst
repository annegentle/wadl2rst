
Create Server Back Up (Createbackup Action)
===========================================

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Creates a back up of a server.

Specify the ``createBackup`` action in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createServerBackUp(CreatebackupAction).yaml

	- tenant_id: tenant_id
	- server_id: server_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../createServerBackUp(CreatebackupAction).yaml

	- createBackup: createBackup




**Example Create Server Back Up (Createbackup Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action-admin/createBackup-req.json
   :language: javascript



Response
^^^^^^^^




