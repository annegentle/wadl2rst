
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




.. rest_parameters:: ../updateCloudpipe.yaml

	- vpn_ip: vpn_ip
	- vpn_port: vpn_port




**Example Update Cloudpipe: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-cloudpipe/cloud-pipe-update-req.json
   :language: javascript



Response
^^^^^^^^



