
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|project_id                |xsd:string *(Required)*  |Creates the cloudpipe    |
|                          |                         |for a project. If        |
|                          |                         |omitted, the project ID  |
|                          |                         |defaults to the calling  |
|                          |                         |tenant.                  |
+--------------------------+-------------------------+-------------------------+





**Example Create Cloudpipe: JSON request**


.. code::

    {
        "cloudpipe": {
            "project_id": "059f21e3-c20e-4efc-9e7a-eba2ab3c6f9a"
        }
    }
    


Response
^^^^^^^^





**Example Create Cloudpipe: JSON request**


.. code::

    {
        "instance_id": "1e9b8425-34af-488e-b969-4d46f4a6382e"
    }
    

