
List Volume Types
=================

`Request <GET_list_volume_types_v2.1_tenant_id_os-volume-types.rst#request>`__
`Response <GET_list_volume_types_v2.1_tenant_id_os-volume-types.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-volume-types

Lists volume types.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|volume_types              |xsd:list *(Required)*    |The ``volume_types``     |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of volume.      |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name of volume.      |
+--------------------------+-------------------------+-------------------------+
|extra_specs               |xsd:dict *(Required)*    |The definition of a      |
|                          |                         |volume type. This is a   |
|                          |                         |group of policies e.g.   |
|                          |                         |provision type. QoS that |
|                          |                         |will be used to define a |
|                          |                         |volume at creation time. |
+--------------------------+-------------------------+-------------------------+





**Example List Volume Types: JSON request**


.. code::

    {
        "volume_types": [
            {
                "id": "289da7f8-6440-407c-9fb4-7db01ec49164",
                "name": "vol-type-001",
                "extra_specs": {
                    "capabilities": "gpu"
                }
            },
            {
                "id": "96c3bda7-c82a-4f50-be73-ca7621794835",
                "name": "vol-type-002",
                "extra_specs": {}
            }
        ]
    }
    

