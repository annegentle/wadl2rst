
Add Network
===========

`Request <POST_add_network_v2.1_tenant_id_os-networks_add.rst#request>`__
`Response <POST_add_network_v2.1_tenant_id_os-networks_add.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-networks/add

Adds a network to a project.

Policy defaults enable only users with the administrative role to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







**Example Add Network: JSON request**


.. code::

    {
        "id": "1"
    }
    


Response
^^^^^^^^




