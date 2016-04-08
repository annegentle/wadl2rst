
List Servers
============

`Request <GET_list_servers_v2_tenant_id_servers_detail.rst#request>`__
`Response <GET_list_servers_v2_tenant_id_servers_detail.rst#response>`__

.. rest_method:: GET /v2/{tenant_id}/servers/detail

Lists servers with detailed config drive information.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: listServers.yaml

	- os-disk-config:diskConfig: os-disk-config:diskConfig




**Example List Servers: JSON request**


.. code::

    

