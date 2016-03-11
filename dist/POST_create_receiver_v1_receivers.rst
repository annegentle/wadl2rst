=============================================================================
Create Receiver -  OpenStack Compute API v2.1
=============================================================================

Create Receiver
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_receiver_v1_receivers.rst#request>`__
`Response <POST_create_receiver_v1_receivers.rst#response>`__

.. code-block:: javascript

    POST /v1/receivers

Creates a receiver.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|receiver                  |xsd:dict *(Required)*    |A map with detailed data |
|                          |                         |for the receiver.        |
|                          |                         |Receiver Create Request  |
|                          |                         |Body``name`` Name for    |
|                          |                         |the receiver (optional). |
|                          |                         |``cluster_id`` Name, ID, |
|                          |                         |or short ID of the       |
|                          |                         |object targeted by the   |
|                          |                         |receiver (required).     |
|                          |                         |``type`` The type of the |
|                          |                         |receiver where the only  |
|                          |                         |valid value is           |
|                          |                         |``webhook`` currently    |
|                          |                         |(required). ``action``   |
|                          |                         |The action to initiate   |
|                          |                         |when the receiver is     |
|                          |                         |triggered. A valid value |
|                          |                         |should be the name of an |
|                          |                         |action that can be       |
|                          |                         |applied on a cluster.    |
|                          |                         |``actor`` A map of key   |
|                          |                         |and value pairs to use   |
|                          |                         |for authentication. If   |
|                          |                         |omitted, the requester   |
|                          |                         |is assumed to be the     |
|                          |                         |actor (optional).        |
|                          |                         |``params`` A map of key  |
|                          |                         |and value pairs to use   |
|                          |                         |for action creation.     |
|                          |                         |Some actions might       |
|                          |                         |require certain input    |
|                          |                         |parameters (optional).   |
+--------------------------+-------------------------+-------------------------+





**Example Create Receiver: JSON request**


.. code::

    {"receiver": {"action": "CLUSTER_SCALE_OUT","cluster_id": "cf99d754-3cdc-47f4-8a29-cd14f02f5436","name": "cluster_inflate","params": {"count": "1"},"type": "webhook"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|receiver                  |xsd:dict *(Required)*    |The receiver details,    |
|                          |                         |such as ``id``,          |
|                          |                         |``name``, ``action``,    |
|                          |                         |and so on.               |
+--------------------------+-------------------------+-------------------------+





**Example Create Receiver: JSON request**


.. code::

    {"receiver": {"action": "CLUSTER_SCALE_OUT","actor": {"trust_id": ["6dc6d336e3fc4c0a951b5698cd1236d9"]},"channel": {"alarm_url": "http://node1:8778/v1/webhooks/e03dd2e5-8f2e-4ec1-8c6a-74ba891e5422/trigger?V=1&count=1"},"cluster_id": "ae63a10b-4a90-452c-aef1-113a0b255ee3","created_at": "2015-06-27T05:09:43","domain": "Default","id": "573aa1ba-bf45-49fd-907d-6b5d6e6adfd3","name": "cluster_inflate","params": {"count": "1"},"project": "6e18cc2bdbeb48a5b3cad2dc499f6804","type": "webhook","updated_at": null,"user": "b4ad2d6e18cc2b9c48049f6dbe8a5b3c"}}

