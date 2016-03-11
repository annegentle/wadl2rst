=============================================================================
List Receivers -  OpenStack Compute API v2.1
=============================================================================

List Receivers
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_receivers_v1_receivers.rst#request>`__
`Response <GET_list_receivers_v1_receivers.rst#response>`__

.. code-block:: javascript

    GET /v1/receivers

Lists all receivers.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^




This table shows the query parameters for the request:

+-------------------------+------------------------+---------------------------+
|Name                     |Type                    |Description                |
+=========================+========================+===========================+
|limit                    |xsd:int *(Required)*    |Requests a page size of    |
|                         |                        |items. Returns a number of |
|                         |                        |items up to a limit value. |
|                         |                        |Use the ``limit``          |
|                         |                        |parameter to make an       |
|                         |                        |initial limited request    |
|                         |                        |and use the ID of the last-|
|                         |                        |seen item from the         |
|                         |                        |response as the ``marker`` |
|                         |                        |parameter value in a       |
|                         |                        |subsequent limited request.|
+-------------------------+------------------------+---------------------------+
|marker                   |xsd:string *(Required)* |The ID of the last-seen    |
|                         |                        |item. Use the ``limit``    |
|                         |                        |parameter to make an       |
|                         |                        |initial limited request    |
|                         |                        |and use the ID of the last-|
|                         |                        |seen item from the         |
|                         |                        |response as the ``marker`` |
|                         |                        |parameter value in a       |
|                         |                        |subsequent limited request.|
+-------------------------+------------------------+---------------------------+
|sort                     |xsd:string *(Required)* |Sorts the response by one  |
|                         |                        |or more attribute and      |
|                         |                        |optional sort direction    |
|                         |                        |combinations. A valid      |
|                         |                        |direction is ``asc``       |
|                         |                        |(ascending) or ``desc``    |
|                         |                        |(descending). Default      |
|                         |                        |direction is ``asc``       |
|                         |                        |(ascending). Specify the   |
|                         |                        |list as < key > [: <       |
|                         |                        |direction > ]. For         |
|                         |                        |example, the following     |
|                         |                        |query parameters in the    |
|                         |                        |URI sort the objects in    |
|                         |                        |the response by ``name``   |
|                         |                        |in ascending order and     |
|                         |                        |then by ``status`` in      |
|                         |                        |descending order: GET      |
|                         |                        |/v2/images?sort=name:asc,  |
|                         |                        |status:descThe following   |
|                         |                        |query parameters in the    |
|                         |                        |URI sort the objects in    |
|                         |                        |the response by ``name``   |
|                         |                        |in descending order and    |
|                         |                        |then by ``status`` in      |
|                         |                        |ascending order. GET       |
|                         |                        |/v2/images?sort=name:desc, |
|                         |                        |status                     |
+-------------------------+------------------------+---------------------------+
|global_project           |xsd:boolean *(Required)*|Indicates whether to       |
|                         |                        |include objects for all    |
|                         |                        |projects or objects for    |
|                         |                        |the current project in the |
|                         |                        |response. If you are an    |
|                         |                        |administrative user and    |
|                         |                        |you set this value to      |
|                         |                        |``True``, the call returns |
|                         |                        |all objects from all       |
|                         |                        |projects. Default is       |
|                         |                        |``False``, which returns   |
|                         |                        |only objects in the        |
|                         |                        |current project.           |
+-------------------------+------------------------+---------------------------+
|name                     |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the name of a receiver.    |
+-------------------------+------------------------+---------------------------+
|type                     |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the type of a receiver.    |
+-------------------------+------------------------+---------------------------+
|user                     |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the user name of a         |
|                         |                        |receiver.                  |
+-------------------------+------------------------+---------------------------+
|cluster_id               |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the ID of the targeted     |
|                         |                        |cluster of a receiver.     |
+-------------------------+------------------------+---------------------------+
|action                   |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the targeted action of a   |
|                         |                        |receiver.                  |
+-------------------------+------------------------+---------------------------+







Response
^^^^^^^^^^^^^^^^^^





**Example List Receivers: JSON request**


.. code::

    {"receivers": [{"action": "CLUSTER_SCALE_OUT","actor": {"trust_id": ["6dc6d336e3fc4c0a951b5698cd1236d9"]},"channel": {"alarm_url": "http://node1:8778/v1/webhooks/e03dd2e5-8f2e-4ec1-8c6a-74ba891e5422/trigger?V=1&count=1"},"cluster_id": "ae63a10b-4a90-452c-aef1-113a0b255ee3","created_at": "2015-06-27T05:09:43","domain": "Default","id": "573aa1ba-bf45-49fd-907d-6b5d6e6adfd3","name": "cluster_inflate","params": {"count": "1"},"project": "6e18cc2bdbeb48a5b3cad2dc499f6804","type": "webhook","updated_at": null,"user": "b4ad2d6e18cc2b9c48049f6dbe8a5b3c"}]}

