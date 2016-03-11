=============================================================================
Show Server Action Details -  OpenStack Compute API v2.1
=============================================================================

Show Server Action Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_server_action_details_v2.1_tenant_id_servers_server_id_os-instance-actions_request_id_.rst#request>`__
`Response <GET_show_server_action_details_v2.1_tenant_id_servers_server_id_os-instance-actions_request_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/os-instance-actions/{request_id}

Shows details for a server action.



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
|{request_id}              |xsd:string               |The ID of the request.   |
+--------------------------+-------------------------+-------------------------+
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Server Action Details: JSON request**


.. code::

    {"instanceAction": {"action": "reboot","events": [{"event": "schedule","finish_time": "2012-12-05T01:02:00.000000","result": "Success","start_time": "2012-12-05T01:00:02.000000","traceback": ""},{"event": "compute_create","finish_time": "2012-12-05T01:04:00.000000","result": "Success","start_time": "2012-12-05T01:03:00.000000","traceback": ""}],"instance_uuid": "b48316c5-71e8-45e4-9884-6c78055b9b13","message": "","project_id": "147","request_id": "req-3293a3f1-b44c-4609-b8d2-d81b105636b8","start_time": "2012-12-05T00:00:00.000000","user_id": "789"}}

