=============================================================================
Evacuate Server (Evacuate Action) -  OpenStack Compute API v2.1
=============================================================================

Evacuate Server (Evacuate Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_evacuate_server_(evacuate_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_evacuate_server_(evacuate_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Evacuates a server from a failed host to a new one.

Specify the ``evacuate`` action in the request body.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
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





This table shows the body parameters for the request:

+-----------------------+-----------------------+------------------------------+
|Name                   |Type                   |Description                   |
+=======================+=======================+==============================+
|evacuate               |xsd:string *(Required)*|Specify the ``evacuate``      |
|                       |                       |action in the request body.   |
+-----------------------+-----------------------+------------------------------+
|host                   |xsd:string *(Required)*|The name or ID of the host to |
|                       |                       |which the server is evacuated.|
+-----------------------+-----------------------+------------------------------+
|adminPass              |xsd:string *(Required)*|An administrative password to |
|                       |                       |access the evacuated          |
|                       |                       |instance. To set the          |
|                       |                       |administrative password, set  |
|                       |                       |the                           |
|                       |                       |``enable_instance_password``  |
|                       |                       |configuration option to       |
|                       |                       |``True``. If you set this     |
|                       |                       |option to ``False`` and you   |
|                       |                       |try to set the administrative |
|                       |                       |password, the API does not    |
|                       |                       |set the password and the      |
|                       |                       |response shows a ``null``     |
|                       |                       |value for the ``adminPass``   |
|                       |                       |parameter.                    |
+-----------------------+-----------------------+------------------------------+





**Example Evacuate Server (Evacuate Action): JSON request**


.. code::

    {
        "evacuate": {
            "host": "b419863b7d814906a68fb31703c0dbd6",
            "adminPass": "MySecretPass"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Evacuate Server (Evacuate Action): JSON request**


.. code::

    {
        "adminPass": "MySecretPass"
    }
    

