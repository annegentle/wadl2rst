
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







Response
^^^^^^^^


.. rest_parameters:: listVolumeTypes.yaml

	- volume_types: volume_types
	- id: id
	- name: name
	- extra_specs: extra_specs




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
    

