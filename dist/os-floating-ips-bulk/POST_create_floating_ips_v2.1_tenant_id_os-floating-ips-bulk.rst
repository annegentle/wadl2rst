
Create Floating Ips
===================

`Request <POST_create_floating_ips_v2.1_tenant_id_os-floating-ips-bulk.rst#request>`__
`Response <POST_create_floating_ips_v2.1_tenant_id_os-floating-ips-bulk.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-floating-ips-bulk

Bulk-creates floating IPs.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|ip_range                  |xsd:string *(Required)*  |The range of IP          |
|                          |                         |addresses to use for     |
|                          |                         |creating floating IPs.   |
+--------------------------+-------------------------+-------------------------+





**Example Create Floating Ips: JSON request**


.. code::

    {
        "floating_ips_bulk_create": {
            "ip_range": "192.168.1.0/24",
            "pool": "nova",
            "interface": "eth0"
        }
    }
    


Response
^^^^^^^^





**Example Create Floating Ips: JSON request**


.. code::

    {
        "floating_ips_bulk_create": {
            "interface": "eth0",
            "ip_range": "192.168.1.0/24",
            "pool": "nova"
        }
    }
    

