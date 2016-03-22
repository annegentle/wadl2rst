=============================================================================
List Floating Ip Addresses -  OpenStack Compute API v2.1
=============================================================================

List Floating Ip Addresses
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_floating_ip_addresses_v2.1_tenant_id_os-floating-ips.rst#request>`__
`Response <GET_list_floating_ip_addresses_v2.1_tenant_id_os-floating-ips.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-floating-ips

Lists floating IP addresses associated with the tenant or account.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Floating Ip Addresses: JSON request**


.. code::

    {
        "floatingips": [
            {
                "router_id": "d23abc8d-2991-4a55-ba98-2aaea84cc72f",
                "tenant_id": "4969c491a3c74ee4af974e6d800c62de",
                "floating_network_id": "376da547-b977-4cfe-9cba-275c80debf57",
                "fixed_ip_address": "10.0.0.3",
                "floating_ip_address": "172.24.4.228",
                "port_id": "ce705c24-c1ef-408a-bda3-7bbd946164ab",
                "id": "2f245a7b-796b-4f26-9cf9-9e82d248fda7",
                "status": "ACTIVE"
            },
            {
                "router_id": null,
                "tenant_id": "4969c491a3c74ee4af974e6d800c62de",
                "floating_network_id": "376da547-b977-4cfe-9cba-275c80debf57",
                "fixed_ip_address": null,
                "floating_ip_address": "172.24.4.227",
                "port_id": null,
                "id": "61cea855-49cb-4846-997d-801b70c71bdd",
                "status": "DOWN"
            }
        ]
    }
    

