
Show Server Group Details
=========================

`Request <GET_show_server_group_details_v2.1_tenant_id_os-server-groups_server_group_id_.rst#request>`__
`Response <GET_show_server_group_details_v2.1_tenant_id_os-server-groups_server_group_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-server-groups/{server_group_id}

Shows details for a server group.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_group_id: server_group_id







Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group            |xsd:string *(Required)*  |Security group object.   |
+--------------------------+-------------------------+-------------------------+





**Example Show Server Group Details: JSON request**


.. code::

    {
        "server_group": {
            "id": "5bbcc3c4-1da2-4437-a48a-66f15b1b13f9",
            "name": "test",
            "policies": [
                "anti-affinity"
            ],
            "members": [],
            "metadata": {}
        }
    }
    

