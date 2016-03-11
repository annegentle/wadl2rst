=============================================================================
Trigger Webhook Action -  OpenStack Compute API v2.1
=============================================================================

Trigger Webhook Action
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_trigger_webhook_action_v1_webhooks_webhook_id_trigger.rst#request>`__
`Response <POST_trigger_webhook_action_v1_webhooks_webhook_id_trigger.rst#response>`__

.. code-block:: javascript

    POST /v1/webhooks/{webhook_id}/trigger

Triggers a webhook receiver.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{webhook_id}              |csapi:UUID *(Required)*  |The UUID of the webhook. |
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|V                         |xsd:string *(Required)*  |The webhook              |
|                          |                         |implementation version   |
|                          |                         |requested.               |
+--------------------------+-------------------------+-------------------------+
|params                    |xsd:dict *(Required)*    |The query string that    |
|                          |                         |forms the inputs to use  |
|                          |                         |for the targeted action. |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^




