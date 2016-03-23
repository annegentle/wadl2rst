=============================================================================
List Tags -  OpenStack Image API v2
=============================================================================

List Tags
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_tags_v2_metadefs_namespaces_tags_namespace_id_.rst#request>`__
`Response <GET_list_tags_v2_metadefs_namespaces_tags_namespace_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/metadefs/namespaces/tags/{namespace_id}

Lists the tag definitions within a namespace.

To manually paginate through the list of tags, use the ``limit`` and ``marker`` parameters.

To sort the results of this operation use the ``sort_key`` and ``sort_dir`` parameters. The API uses the natural sort order of the tag attribute of the ``sort_key`` parameter.



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
|{namespace_id}            |csapi:UUID               |The UUID of the          |
|                          |                         |namespace.               |
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|limit                     |xsd:int *(Required)*     |Requests a page size of  |
|                          |                         |items. Returns a number  |
|                          |                         |of items up to a limit   |
|                          |                         |value. Use the ``limit`` |
|                          |                         |parameter to make an     |
|                          |                         |initial limited request  |
|                          |                         |and use the ID of the    |
|                          |                         |last-seen item from the  |
|                          |                         |response as the          |
|                          |                         |``marker`` parameter     |
|                          |                         |value in a subsequent    |
|                          |                         |limited request.         |
+--------------------------+-------------------------+-------------------------+
|marker                    |xsd:string *(Required)*  |The ID of the last-seen  |
|                          |                         |item. Use the ``limit``  |
|                          |                         |parameter to make an     |
|                          |                         |initial limited request  |
|                          |                         |and use the ID of the    |
|                          |                         |last-seen item from the  |
|                          |                         |response as the          |
|                          |                         |``marker`` parameter     |
|                          |                         |value in a subsequent    |
|                          |                         |limited request.         |
+--------------------------+-------------------------+-------------------------+
|sort_key                  |xsd:string *(Required)*  |Sorts the response by an |
|                          |                         |attribute, such as       |
|                          |                         |``name``, ``id``, or     |
|                          |                         |``updated_at``. Default  |
|                          |                         |is ``created_at``. The   |
|                          |                         |API uses the natural     |
|                          |                         |sorting direction of the |
|                          |                         |``sort_key`` image       |
|                          |                         |attribute.               |
+--------------------------+-------------------------+-------------------------+
|sort_dir                  |xsd:string *(Required)*  |Sorts the response by a  |
|                          |                         |set of one or more sort  |
|                          |                         |direction and attribute  |
|                          |                         |( ``sort_key`` )         |
|                          |                         |combinations. A valid    |
|                          |                         |value for the sort       |
|                          |                         |direction is ``asc``     |
|                          |                         |(ascending) or ``desc``  |
|                          |                         |(descending). If you     |
|                          |                         |omit the sort direction  |
|                          |                         |in a set, the default is |
|                          |                         |``desc``.                |
+--------------------------+-------------------------+-------------------------+




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|namespace                 |xsd:string *(Required)*  |The namespace is unique  |
|                          |                         |across all users.        |
+--------------------------+-------------------------+-------------------------+





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





**Example List Tags: JSON request**


.. code::

    {
        "tags": [
            {
                "name": "sample-tag1"
            },
            {
                "name": "sample-tag2"
            },
            {
                "name": "sample-tag3"
            }
        ]
    }
    

