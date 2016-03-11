=============================================================================
Update Tag Definition -  OpenStack Compute API v2.1
=============================================================================

Update Tag Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_tag_definition_v2_metadefs_namespaces_tags_namespace_id_tag_name_.rst#request>`__
`Response <PUT_update_tag_definition_v2_metadefs_namespaces_tags_namespace_id_tag_name_.rst#response>`__

.. code-block:: javascript

    PUT /v2/metadefs/namespaces/tags/{namespace_id}/{tag_name}

Renames a tag definition.



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
|{tag_name}                |xsd:string               |The name of the tag.     |
+--------------------------+-------------------------+-------------------------+
|{namespace_id}            |csapi:UUID               |The UUID of the          |
|                          |                         |namespace.               |
+--------------------------+-------------------------+-------------------------+








**Example Update Tag Definition: JSON request**


.. code::

    {"name": "new-tag-name"}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The name of the tag.     |
+--------------------------+-------------------------+-------------------------+





**Example Update Tag Definition: JSON request**


.. code::

    {"name": "new-tag-name"}

