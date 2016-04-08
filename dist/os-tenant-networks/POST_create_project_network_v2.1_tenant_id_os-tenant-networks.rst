
Create Project Network
======================

`Request <POST_create_project_network_v2.1_tenant_id_os-tenant-networks.rst#request>`__
`Response <POST_create_project_network_v2.1_tenant_id_os-tenant-networks.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-tenant-networks

Creates a project network.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Create Project Network: JSON request**


.. code::

    {
        "network": {
            "label": "public",
            "cidr": "172.0.0.0/24",
            "vlan_start": 1,
            "num_networks": 1,
            "network_size": 255
        }
    }
    


Response
^^^^^^^^





**Example Create Project Network: JSON request**


.. code::

    {
        "network": {
            "cidr": "172.0.0.0/24",
            "id": "5bbcc3c4-1da2-4437-a48a-66f15b1b13f9",
            "label": "public"
        }
    }
    

