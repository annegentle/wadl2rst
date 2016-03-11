=============================================================================
Update Agent Build -  OpenStack Compute API v2.1
=============================================================================

Update Agent Build
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_agent_build_v2.1_tenant_id_os-agents_agent_build_id_.rst#request>`__
`Response <PUT_update_agent_build_v2.1_tenant_id_os-agents_agent_build_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/os-agents/{agent_build_id}

Updates an agent build.



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
|{agent_build_id}          |csapi:UUID               |The UUID of the agent    |
|                          |                         |build.                   |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|url                       |xsd:string *(Required)*  |The URL associated with  |
|                          |                         |the agent.               |
+--------------------------+-------------------------+-------------------------+
|md5hash                   |xsd:string *(Required)*  |The MD5 hash.            |
+--------------------------+-------------------------+-------------------------+
|version                   |xsd:string *(Required)*  |The version.             |
+--------------------------+-------------------------+-------------------------+





**Example Update Agent Build: JSON request**


.. code::

    {
        "para": {
            "url": "http://example.com/path/to/resource",
            "md5hash": "add6bb58e139be103324d04d82d8f545",
            "version": "7.0"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|agent_id                  |xsd:int *(Required)*     |The agent ID.            |
+--------------------------+-------------------------+-------------------------+
|url                       |xsd:string *(Required)*  |The URL associated with  |
|                          |                         |the agent.               |
+--------------------------+-------------------------+-------------------------+
|md5hash                   |xsd:string *(Required)*  |The MD5 hash.            |
+--------------------------+-------------------------+-------------------------+
|version                   |xsd:string *(Required)*  |The version.             |
+--------------------------+-------------------------+-------------------------+





**Example Update Agent Build: JSON request**


.. code::

    {
        "agent": {
            "agent_id": "1",
            "md5hash": "add6bb58e139be103324d04d82d8f545",
            "url": "http://example.com/path/to/resource",
            "version": "7.0"
        }
    }
    

