
Ping Instances
==============

`Request <GET_ping_instances_v2.1_tenant_id_os-fping.rst#request>`__
`Response <GET_ping_instances_v2.1_tenant_id_os-fping.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-fping

Run the fping utility to ping instances and report which ones are alive.

Specify the ``all_tenants=1`` query parameter to ping instances for all tenants. For example:

GET /os-fping?all_tenants=1Specify the ``include`` and ``exclude`` query parameters to filter the results. For example:

GET /os-fping?all_tenants=1&include=uuid1,uuid2&exclude=uuid3,uuid4Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id


This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|all_tenants               |xsd:int *(Required)*     |Specify the              |
|                          |                         |``all_tenants=1`` query  |
|                          |                         |parameter to ping        |
|                          |                         |instances for all        |
|                          |                         |tenants.                 |
+--------------------------+-------------------------+-------------------------+
|include                   |xsd:string *(Required)*  |Specify ``include=uuid[, |
|                          |                         |uuid...]`` to include    |
|                          |                         |the instances in the     |
|                          |                         |results.                 |
+--------------------------+-------------------------+-------------------------+
|exclude                   |xsd:string *(Required)*  |Specify ``exclude=uuid[, |
|                          |                         |uuid...]`` to exclude    |
|                          |                         |the instances from the   |
|                          |                         |results.                 |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^





**Example Ping Instances: JSON request**


.. code::

    {
        "servers": [
            {
                "alive": false,
                "id": "1d1aea35-472b-40cf-9337-8eb68480aaa1",
                "project_id": "openstack"
            }
        ]
    }
    

