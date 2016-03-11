=============================================================================
List All Metadata -  OpenStack Compute API v2.1
=============================================================================

List All Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_all_metadata_v2.1_tenant_id_servers_server_id_metadata.rst#request>`__
`Response <GET_list_all_metadata_v2.1_tenant_id_servers_server_id_metadata.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/metadata

Lists all metadata for a server.

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








Response
^^^^^^^^^^^^^^^^^^





**Example List All Metadata: JSON request**


.. code::

    {
        "metadata": {
            "foo": "Foo Value"
        }
    }
    

