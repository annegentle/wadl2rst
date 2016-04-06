
List Actions For Server
=======================

`Request <GET_list_actions_for_server_v2.1_tenant_id_servers_server_id_os-instance-actions.rst#request>`__
`Response <GET_list_actions_for_server_v2.1_tenant_id_servers_server_id_os-instance-actions.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-instance-actions

Lists actions for a server.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id







Response
^^^^^^^^





**Example List Actions For Server: JSON request**


.. code::

    {
        "instanceActions": [
            {
                "action": "resize",
                "instance_uuid": "b48316c5-71e8-45e4-9884-6c78055b9b13",
                "message": "",
                "project_id": "842",
                "request_id": "req-25517360-b757-47d3-be45-0e8d2a01b36a",
                "start_time": "2012-12-05T01:00:00.000000",
                "user_id": "789"
            },
            {
                "action": "reboot",
                "instance_uuid": "b48316c5-71e8-45e4-9884-6c78055b9b13",
                "message": "",
                "project_id": "147",
                "request_id": "req-3293a3f1-b44c-4609-b8d2-d81b105636b8",
                "start_time": "2012-12-05T00:00:00.000000",
                "user_id": "789"
            }
        ]
    }
    

