=============================================================================
Update Namespace -  OpenStack Image API v2
=============================================================================

Update Namespace
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_namespace_v2_metadefs_namespaces_namespace_id_.rst#request>`__
`Response <PUT_update_namespace_v2_metadefs_namespaces_namespace_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2/metadefs/namespaces/{namespace_id}

Updates a namespace.



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








**Example Update Namespace: JSON request**


.. code::

    {
        "description": "Choose capabilities that should be provided by the Compute Host. This provides the ability to fine tune the hardware specification required when a new vm is requested.",
        "display_name": "Hypervisor Selection",
        "namespace": "OS::Compute::Hypervisor",
        "protected": false,
        "visibility": "public"
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Update Namespace: JSON request**


.. code::

    {
        "created_at": "2014-09-19T13:31:37Z",
        "description": "Choose capabilities that should be provided by the Compute Host. This provides the ability to fine tune the harware specification required when a new vm is requested.",
        "display_name": "Hypervisor Selection",
        "namespace": "OS::Compute::Hypervisor",
        "owner": "7ec22942411e427692e8a3436be1031a",
        "protected": false,
        "schema": "/v2/schemas/metadefs/namespace",
        "self": "/v2/metadefs/namespaces/OS::Compute::Hypervisor",
        "updated_at": "2014-09-19T13:31:37Z",
        "visibility": "public"
    }
    

