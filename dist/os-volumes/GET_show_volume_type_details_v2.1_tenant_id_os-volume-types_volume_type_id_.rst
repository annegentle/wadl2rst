
Show Volume Type Details
========================

`Request <GET_show_volume_type_details_v2.1_tenant_id_os-volume-types_volume_type_id_.rst#request>`__
`Response <GET_show_volume_type_details_v2.1_tenant_id_os-volume-types_volume_type_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-volume-types/{volume_type_id}

Shows details for a volume type.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Volume Type Details: JSON request**


.. code::

    {
        "volume_type": {
            "id": "289da7f8-6440-407c-9fb4-7db01ec49164",
            "name": "vol-type-001",
            "extra_specs": {
                "capabilities": "gpu"
            }
        }
    }
    

