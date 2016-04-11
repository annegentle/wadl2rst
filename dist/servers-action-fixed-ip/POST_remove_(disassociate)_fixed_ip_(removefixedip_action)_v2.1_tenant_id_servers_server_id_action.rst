
Remove (Disassociate) Fixed Ip (Removefixedip Action)
=====================================================

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Removes, or disassociates, a fixed IP address from a server.

Specify the ``removeFixedIp`` action in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202,,503,400,401,403,405,404,415,400,503,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../remove(Disassociate)FixedIp(RemovefixedipAction).yaml

	- tenant_id: tenant_id
	- server_id: server_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../remove(Disassociate)FixedIp(RemovefixedipAction).yaml

	- removeFixedIp: removeFixedIp




**Example Remove (Disassociate) Fixed Ip (Removefixedip Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/multinic-remove-fixed-ip-req.json
   :language: javascript



Response
^^^^^^^^




