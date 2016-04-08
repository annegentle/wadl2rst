
Ping An Instance
================

`Request <GET_ping_an_instance_v2.1_tenant_id_os-fping_instance_id_.rst#request>`__
`Response <GET_ping_an_instance_v2.1_tenant_id_os-fping_instance_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-fping/{instance_id}

Run the fping utility to ping an instance and report whether it is alive.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Ping An Instance: JSON request**


.. code::

    {
        "server": {
            "alive": false,
            "id": "f5e6fd6d-c0a3-4f9e-aabf-d69196b6d11a",
            "project_id": "openstack"
        }
    }
    

