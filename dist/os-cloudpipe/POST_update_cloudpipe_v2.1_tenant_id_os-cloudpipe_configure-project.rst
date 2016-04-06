
Update Cloudpipe
================

`Request <POST_update_cloudpipe_v2.1_tenant_id_os-cloudpipe_configure-project.rst#request>`__
`Response <POST_update_cloudpipe_v2.1_tenant_id_os-cloudpipe_configure-project.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-cloudpipe/configure-project

Updates the virtual private network (VPN) IP address and port for a cloudpipe instance.



Normal response codes: 202,,503,400,401,403,405,415,400

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
|vpn_ip                    |xsd:string *(Required)*  |The VPN IP address.      |
+--------------------------+-------------------------+-------------------------+
|vpn_port                  |xsd:string *(Required)*  |The VPN port.            |
+--------------------------+-------------------------+-------------------------+





**Example Update Cloudpipe: JSON request**


.. code::

    {
        "configure_project": {
            "vpn_ip": "192.168.1.1",
            "vpn_port": "2000"
        }
    }
    


Response
^^^^^^^^




