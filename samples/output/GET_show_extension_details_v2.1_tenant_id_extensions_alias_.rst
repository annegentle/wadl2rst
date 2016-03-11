=============================================================================
Show Extension Details -  OpenStack Compute API v2.1
=============================================================================

Show Extension Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_extension_details_v2.1_tenant_id_extensions_alias_.rst#request>`__
`Response <GET_show_extension_details_v2.1_tenant_id_extensions_alias_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/extensions/{alias}

Shows details for an extension, by alias.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|203                       |                         |                         |
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
|{alias}                   |xsd:string               |An alias for the         |
|                          |                         |extension name. For      |
|                          |                         |example, ``os-server-    |
|                          |                         |external-events``.       |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Extension Details: JSON request**


.. code::

    {
        "extension": {
            "updated": "2014-12-03T00:00:00Z",
            "name": "ServerExternalEvents",
            "links": [],
            "namespace": "http://docs.openstack.org/compute/ext/fake_xml",
            "alias": "os-server-external-events",
            "description": "Server External Event Triggers."
        }
    }
    

