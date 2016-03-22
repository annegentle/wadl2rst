=============================================================================
List Actions For Server -  OpenStack Compute API v2.1
=============================================================================

List Actions For Server
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_actions_for_server_v2.1_tenant_id_servers_server_id_os-instance-actions.rst#request>`__
`Response <GET_list_actions_for_server_v2.1_tenant_id_servers_server_id_os-instance-actions.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/os-instance-actions

Lists actions for a server.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





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
    

