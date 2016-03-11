=============================================================================
Show Receiver Details -  OpenStack Compute API v2.1
=============================================================================

Show Receiver Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_receiver_details_v1_receivers_receiver_id_.rst#request>`__
`Response <GET_show_receiver_details_v1_receivers_receiver_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/receivers/{receiver_id}

Shows details for a receiver.



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
|{receiver_id}             |csapi:UUID *(Required)*  |The UUID of the receiver.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Receiver Details: JSON request**


.. code::

    {"receiver": {"action": "CLUSTER_SCALE_OUT","actor": {"trust_id": ["6dc6d336e3fc4c0a951b5698cd1236d9"]},"channel": {"alarm_url": "http://node1:8778/v1/webhooks/e03dd2e5-8f2e-4ec1-8c6a-74ba891e5422/trigger?V=1&count=1"},"cluster_id": "ae63a10b-4a90-452c-aef1-113a0b255ee3","created_at": "2015-06-27T05:09:43","domain": "Default","id": "573aa1ba-bf45-49fd-907d-6b5d6e6adfd3","name": "cluster_inflate","params": {"count": "1"},"project": "6e18cc2bdbeb48a5b3cad2dc499f6804","type": "webhook","updated_at": null,"user": "b4ad2d6e18cc2b9c48049f6dbe8a5b3c"}}

