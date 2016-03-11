=============================================================================
Create Tags -  OpenStack Compute API v2.1
=============================================================================

Create Tags
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_tags_v2_metadefs_namespaces_tags_namespace_id_.rst#request>`__
`Response <POST_create_tags_v2_metadefs_namespaces_tags_namespace_id_.rst#response>`__

.. code-block:: javascript

    POST /v2/metadefs/namespaces/tags/{namespace_id}

Creates one or more tag definitions in a namespace.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{namespace_id}            |csapi:UUID               |The UUID of the          |
|                          |                         |namespace.               |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|namespace                 |xsd:string *(Required)*  |The namespace is unique  |
|                          |                         |across all users.        |
+--------------------------+-------------------------+-------------------------+
|tags                      |xsd:list *(Required)*    |A list of ``tag``        |
|                          |                         |objects.                 |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name of the tag.     |
+--------------------------+-------------------------+-------------------------+





**Example Create Tags: JSON request**


.. code::

    {"tags": [{"name": "sample-tag1"},{"name": "sample-tag2"},{"name": "sample-tag3"}]}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|tags                      |xsd:list *(Required)*    |A list of ``tag``        |
|                          |                         |objects.                 |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name of the tag.     |
+--------------------------+-------------------------+-------------------------+





**Example Create Tags: JSON request**


.. code::

    {"tags": [{"name": "sample-tag1"},{"name": "sample-tag2"},{"name": "sample-tag3"}]}

