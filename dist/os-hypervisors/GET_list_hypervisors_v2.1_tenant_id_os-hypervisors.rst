
List Hypervisors
================

`Request <GET_list_hypervisors_v2.1_tenant_id_os-hypervisors.rst#request>`__
`Response <GET_list_hypervisors_v2.1_tenant_id_os-hypervisors.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-hypervisors

Lists hypervisors.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^





**Example List Hypervisors: JSON request**


.. code::

    {
        "hypervisors": [
            {
                "status": "enabled",
                "state": "up",
                "id": 1,
                "hypervisor_hostname": "fake-mini"
            }
        ]
    }
    

