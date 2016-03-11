=============================================================================
Show Action Details -  OpenStack Compute API v2.1
=============================================================================

Show Action Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_action_details_v1_actions_action_id_.rst#request>`__
`Response <GET_show_action_details_v1_actions_action_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/actions/{action_id}

Shows details for an action.



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
|{action_id}               |csapi:UUID *(Required)*  |The UUID of the action.  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Action Details: JSON request**


.. code::

    {"action": "CLUSTER_DELETE","cause": "RPC Request","context": {},"created_at": "2015-06-27T05:09:43","depended_by": [],"depends_on": [],"end_time": 1423570000.0,"id": "ffbb9175-d510-4bc1-b676-c6aba2a4ca81","inputs": {},"interval": -1,"name": "cluster_delete_fcc9b635","outputs": {},"owner": null,"start_time": 1423570000.0,"status": "FAILED","status_reason": "Cluster action FAILED","target": "fcc9b635-52e3-490b-99f2-87b1640e4e89","timeout": 3600,"updated_at": null}

