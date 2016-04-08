
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




.. rest_parameters:: runEvents.yaml

	- events: events
	- name: name
	- tag: tag
	- server_uuid: server_uuid
	- status: status




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


.. rest_parameters:: runEvents.yaml

	- events: events
	- code: code
	- name: name
	- server_uuid: server_uuid
	- status: status
	- tag: tag




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
    

