
Create Or Replace Metadata Items
================================

`Request <PUT_create_or_replace_metadata_items_v2.1_tenant_id_servers_server_id_metadata.rst#request>`__
`Response <PUT_create_or_replace_metadata_items_v2.1_tenant_id_servers_server_id_metadata.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/servers/{server_id}/metadata

Creates or replaces one or more metadata items for a server.

Creates any metadata items that do not already exist in the server. Removes and completely replaces any metadata items that already exist in the server with the metadata items in the request.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Create Or Replace Metadata Items: JSON request**


.. code::

    {
        "metadata": {
            "foo": "Foo Value"
        }
    }
    


Response
^^^^^^^^





**Example Create Or Replace Metadata Items: JSON request**


.. code::

    {
        "metadata": {
            "foo": "Foo Value"
        }
    }
    

