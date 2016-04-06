
Show Server Details
===================

`Request <GET_show_server_details_v2_tenant_id_servers_server_id_.rst#request>`__
`Response <GET_show_server_details_v2_tenant_id_servers_server_id_.rst#response>`__

.. rest_method:: GET /v2/{tenant_id}/servers/{server_id}

Shows details for a server.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- os-disk-config:diskConfig: os-disk-config:diskConfig
	- server_id: server_id







Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-disk-config:diskConfig |xsd:string               |Valid value is ``AUTO``  |
|                          |                         |or ``MANUAL``.           |
+--------------------------+-------------------------+-------------------------+





**Example Show Server Details: JSON request**


.. code::

    

