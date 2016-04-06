
Run Events
==========

`Request <POST_run_events_v2.1_tenant_id_os-server-external-events.rst#request>`__
`Response <POST_run_events_v2.1_tenant_id_os-server-external-events.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-server-external-events

Creates one or more external events, which the API dispatches to the instance.

You must assign this instance to a host. Otherwise, this call does not dispatch the event to the instance.



Normal response codes: 200

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
|events                    |xsd:list *(Required)*    |The action.              |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The event name. A valid  |
|                          |                         |value is ``network-      |
|                          |                         |changed``, ``network-vif-|
|                          |                         |plugged``, ``network-vif-|
|                          |                         |unplugged``, or          |
|                          |                         |``network-vif-deleted``. |
+--------------------------+-------------------------+-------------------------+
|tag                       |xsd:string *(Required)*  |A string value that      |
|                          |                         |identifies the event.    |
+--------------------------+-------------------------+-------------------------+
|server_uuid               |csapi:UUID *(Required)*  |The UUID of the server   |
|                          |                         |instance to which the    |
|                          |                         |API dispatches the       |
|                          |                         |event. You must assign   |
|                          |                         |this instance to a host. |
|                          |                         |Otherwise, this call     |
|                          |                         |does not dispatch the    |
|                          |                         |event to the instance.   |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |The event status. A      |
|                          |                         |valid value is           |
|                          |                         |``failed``,              |
|                          |                         |``completed``, or ``in-  |
|                          |                         |progress``. Default is   |
|                          |                         |``completed``.           |
+--------------------------+-------------------------+-------------------------+





**Example Run Events: JSON request**


.. code::

    {
        "events": [
            {
                "name": "test-event",
                "tag": "foo",
                "status": "completed",
                "server_uuid": "3df201cf-2451-44f2-8d25-a4ca826fc1f3"
            }
        ]
    }
    


Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|events                    |xsd:list *(Required)*    |The action.              |
+--------------------------+-------------------------+-------------------------+
|code                      |xsd:string *(Required)*  |The HTTP response code   |
|                          |                         |for the event.           |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The event name. A valid  |
|                          |                         |value is ``network-      |
|                          |                         |changed``, ``network-vif-|
|                          |                         |plugged``, ``network-vif-|
|                          |                         |unplugged``, or          |
|                          |                         |``network-vif-deleted``. |
+--------------------------+-------------------------+-------------------------+
|server_uuid               |csapi:UUID *(Required)*  |The UUID of the server   |
|                          |                         |instance to which the    |
|                          |                         |API dispatches the       |
|                          |                         |event. You must assign   |
|                          |                         |this instance to a host. |
|                          |                         |Otherwise, this call     |
|                          |                         |does not dispatch the    |
|                          |                         |event to the instance.   |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |The event status. A      |
|                          |                         |valid value is           |
|                          |                         |``failed``,              |
|                          |                         |``completed``, or ``in-  |
|                          |                         |progress``. Default is   |
|                          |                         |``completed``.           |
+--------------------------+-------------------------+-------------------------+
|tag                       |xsd:string *(Required)*  |A string value that      |
|                          |                         |identifies the event.    |
+--------------------------+-------------------------+-------------------------+





**Example Run Events: JSON request**


.. code::

    {
        "events": [
            {
                "code": 200,
                "name": "network-changed",
                "server_uuid": "ff1df7b2-6772-45fd-9326-c0a3b05591c2",
                "status": "completed",
                "tag": "foo"
            }
        ]
    }
    

