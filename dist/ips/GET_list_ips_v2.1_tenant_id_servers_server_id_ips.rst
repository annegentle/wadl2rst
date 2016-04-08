
List Ips
========

`Request <GET_list_ips_v2.1_tenant_id_servers_server_id_ips.rst#request>`__
`Response <GET_list_ips_v2.1_tenant_id_servers_server_id_ips.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/ips

Lists IP addresses that are assigned to an instance.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Ips: JSON request**


.. code::

    {
        "addresses": {
            "private": [
                {
                    "addr": "192.168.0.3",
                    "version": 4
                }
            ]
        }
    }
    

