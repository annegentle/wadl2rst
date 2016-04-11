
Create Cloudpipe
================

`Request <POST_create_cloudpipe_v2.1_tenant_id_os-cloudpipe.rst#request>`__
`Response <POST_create_cloudpipe_v2.1_tenant_id_os-cloudpipe.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-cloudpipe

Creates a cloudpipe.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../createCloudpipe.yaml

	- project_id: project_id




**Example Create Cloudpipe: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-cloudpipe/cloud-pipe-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Cloudpipe: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-cloudpipe/cloud-pipe-create-resp.json
   :language: javascript

