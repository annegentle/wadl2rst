=============================================================================
Create Or Update Metadata Item -  OpenStack Compute API v2.1
=============================================================================

Create Or Update Metadata Item
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_create_or_update_metadata_item_v2.1_tenant_id_servers_server_id_metadata_key_.rst#request>`__
`Response <PUT_create_or_update_metadata_item_v2.1_tenant_id_servers_server_id_metadata_key_.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/servers/{server_id}/metadata/{key}

Creates or replaces a metadata item, by key, for a server.

Creates a metadata item that does not already exist in the server. Removes and completely replaces a metadata item that already exists in the server with the metadata item in the request.

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








**Example Create Or Update Metadata Item: JSON request**


.. code::

    {
        "meta": {
            "foo": "Bar Value"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Or Update Metadata Item: JSON request**


.. code::

    {
        "meta": {
            "foo": "Bar Value"
        }
    }
    

