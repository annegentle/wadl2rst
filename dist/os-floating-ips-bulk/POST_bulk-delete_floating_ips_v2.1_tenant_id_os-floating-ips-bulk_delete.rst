
Bulk-Delete Floating Ips
========================

`Request <POST_bulk-delete_floating_ips_v2.1_tenant_id_os-floating-ips-bulk_delete.rst#request>`__
`Response <POST_bulk-delete_floating_ips_v2.1_tenant_id_os-floating-ips-bulk_delete.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-floating-ips-bulk/delete

Bulk-deletes floating IPs.



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
|                          |                         |addresses from which to  |
|                          |                         |bulk-delete floating IPs.|
+--------------------------+-------------------------+-------------------------+





**Example Bulk-Delete Floating Ips: JSON request**


.. code::

    {
        "ip_range": "192.168.1.0/24"
    }
    


Response
^^^^^^^^





**Example Bulk-Delete Floating Ips: JSON request**


.. code::

    {
        "floating_ips_bulk_delete": "192.168.1.0/24"
    }
    

