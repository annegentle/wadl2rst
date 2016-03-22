=============================================================================
Show Metadata Item Details -  OpenStack Compute API v2.1
=============================================================================

Show Metadata Item Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_metadata_item_details_v2.1_tenant_id_servers_server_id_metadata_key_.rst#request>`__
`Response <GET_show_metadata_item_details_v2.1_tenant_id_servers_server_id_metadata_key_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/metadata/{key}

Shows details for a metadata item, by key, for a server.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+
|{key}                     |xsd:string               |The metadata item key,   |
|                          |                         |as a string. Maximum     |
|                          |                         |length is 255 characters.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Metadata Item Details: JSON request**


.. code::

    {
        "meta": {
            "foo": "Foo Value"
        }
    }
    

