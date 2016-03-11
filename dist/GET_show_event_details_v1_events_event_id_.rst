=============================================================================
Show Event Details -  OpenStack Compute API v2.1
=============================================================================

Show Event Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_event_details_v1_events_event_id_.rst#request>`__
`Response <GET_show_event_details_v1_events_event_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/events/{event_id}

Shows details for an event.



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
|{event_id}                |csapi:UUID *(Required)*  |The UUID of the event.   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Event Details: JSON request**


.. code::

    {"event": {"action": "create","cluster_id": null,"id": "2d255b9c-8f36-41a2-a137-c0175ccc29c3","level": "20","obj_id": "0df0931b-e251-4f2e-8719-4ebfda3627ba","obj_name": "node009","obj_type": "NODE","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","status": "CREATING","status_reason": "Initializing","timestamp": "2015-03-05T08:53:15","user": "a21ded6060534d99840658a777c2af5a"}}

