=============================================================================
Show Image Member Schema -  OpenStack Image API v2
=============================================================================

Show Image Member Schema
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_image_member_schema_v2_schemas_member.rst#request>`__
`Response <GET_show_image_member_schema_v2_schemas_member.rst#response>`__

.. code-block:: javascript

    GET /v2/schemas/member

(Since Images v2.1) Shows a JSON schema document that represents an image member entity.

The following schema is solely an example. Consider only the response to the API call as authoritative.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









Response
^^^^^^^^^^^^^^^^^^





**Example Show Image Member Schema: JSON request**


.. code::

    {
        "name": "member",
        "properties": {
            "created_at": {
                "description": "Date and time of image member creation",
                "type": "string"
            },
            "image_id": {
                "description": "An identifier for the image",
                "pattern": "^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}-([0-9a-fA-F]){12}$",
                "type": "string"
            },
            "member_id": {
                "description": "An identifier for the image member (tenantId)",
                "type": "string"
            },
            "schema": {
                "type": "string"
            },
            "status": {
                "description": "The status of this image member",
                "enum": [
                    "pending",
                    "accepted",
                    "rejected"
                ],
                "type": "string"
            },
            "updated_at": {
                "description": "Date and time of last modification of image member",
                "type": "string"
            }
        }
    }
    

