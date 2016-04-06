
Disassociate Project
====================

`Request <POST_disassociate_project_v2.1_tenant_id_os-networks_network_id_action.rst#request>`__
`Response <POST_disassociate_project_v2.1_tenant_id_os-networks_network_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-networks/{network_id}/action

Disassociates a project from a network.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- network_id: network_id







**Example Disassociate Project: JSON request**


.. code::

    {
        "disassociate_project": null
    }
    


Response
^^^^^^^^




