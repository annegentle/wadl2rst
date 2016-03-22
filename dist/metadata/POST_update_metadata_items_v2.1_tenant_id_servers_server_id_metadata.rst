=============================================================================
Update Metadata Items -  OpenStack Compute API v2.1
=============================================================================

Update Metadata Items
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_update_metadata_items_v2.1_tenant_id_servers_server_id_metadata.rst#request>`__
`Response <POST_update_metadata_items_v2.1_tenant_id_servers_server_id_metadata.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/metadata

Updates one or more metadata items for a server.

Replaces metadata items that match keys. Does not modify items that are not in the request.

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








**Example Update Metadata Items: JSON request**


.. code::

    {
        "metadata": {
            "foo": "Foo Value"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Update Metadata Items: JSON request**


.. code::

    {
        "metadata": {
            "foo": "Foo Value"
        }
    }
    

