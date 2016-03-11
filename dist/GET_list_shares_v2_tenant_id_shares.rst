=============================================================================
List Shares -  OpenStack Compute API v2.1
=============================================================================

List Shares
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_shares_v2_tenant_id_shares.rst#request>`__
`Response <GET_list_shares_v2_tenant_id_shares.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/shares

Lists all shares.



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
|X-Openstack-Manila-Api-   |xsd:string               |The HTTP header to       |
|Version                   |                         |specify a valid Shared   |
|                          |                         |File Systems API micro-  |
|                          |                         |version. For example,    |
|                          |                         |``"X-Openstack-Manila-   |
|                          |                         |Api-Version: 2.6"``. If  |
|                          |                         |you omit this header,    |
|                          |                         |the default micro-       |
|                          |                         |version is 2.0.          |
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+---------------------+---------------+----------------------------------------+
|Name                 |Type           |Description                             |
+=====================+===============+========================================+
|all_tenants          |xsd:bool       |(Admin only). Defines whether to list   |
|                     |*(Required)*   |shares for all tenants. Set to ``1`` to |
|                     |               |list shares for all tenants. Set to     |
|                     |               |``0`` to list shares only for the       |
|                     |               |current tenant.                         |
+---------------------+---------------+----------------------------------------+
|name                 |xsd:string     |The share name.                         |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|status               |xsd:string     |Filters by a share status. A valid      |
|                     |*(Required)*   |value is ``creating``, ``error``,       |
|                     |               |``available``, ``deleting``,            |
|                     |               |``error_deleting``,                     |
|                     |               |``manage_starting``, ``manage_error``,  |
|                     |               |``unmanage_starting``,                  |
|                     |               |``unmanage_error``, ``unmanaged``,      |
|                     |               |``extending``, ``extending_error``,     |
|                     |               |``shrinking``, ``shrinking_error``, or  |
|                     |               |``shrinking_possible_data_loss_error``. |
+---------------------+---------------+----------------------------------------+
|share_server_id      |csapi:UUID     |The UUID of the share server.           |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|metadata             |xsd:dict       |One or more metadata key-value pairs,   |
|                     |*(Required)*   |as a dictionary of strings.             |
+---------------------+---------------+----------------------------------------+
|extra_specs          |xsd:string     |The extra specifications as a set of    |
|                     |*(Required)*   |one or more key-value pairs. In each    |
|                     |               |pair, the key is the name of the extra  |
|                     |               |specification and the value is the      |
|                     |               |share type that was used to create the  |
|                     |               |share.                                  |
+---------------------+---------------+----------------------------------------+
|share_type_id        |csapi:UUID     |(Since API v2.6.) The UUID of the share |
|                     |*(Required)*   |type.                                   |
+---------------------+---------------+----------------------------------------+
|limit                |xsd:int        |The maximum number of shares to return. |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|offset               |xsd:int        |The offset to define start point of     |
|                     |*(Required)*   |share listing.                          |
+---------------------+---------------+----------------------------------------+
|sort_key             |xsd:string     |The key to sort a list of shares. A     |
|                     |*(Required)*   |valid value is ``id``, ``status``,      |
|                     |               |``size``, ``host``, ``share_proto``,    |
|                     |               |``export_location``,                    |
|                     |               |``availability_zone``, ``user_id``,     |
|                     |               |``project_id``, ``created_at``,         |
|                     |               |``updated_at``, ``display_name``,       |
|                     |               |``name``, ``share_type_id``,            |
|                     |               |``share_type``, ``share_network_id``,   |
|                     |               |``share_network``, ``snapshot_id``, or  |
|                     |               |``snapshot``.                           |
+---------------------+---------------+----------------------------------------+
|sort_dir             |xsd:string     |The direction to sort a list of shares. |
|                     |*(Required)*   |A valid value is ``asc``, or ``desc``.  |
+---------------------+---------------+----------------------------------------+
|snapshot_id          |csapi:UUID     |The UUID of the snapshot that was used  |
|                     |*(Required)*   |to create the share.                    |
+---------------------+---------------+----------------------------------------+
|host                 |xsd:string     |The share host name.                    |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|share_network_id     |csapi:UUID     |The UUID of the share network.          |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|project_id           |csapi:UUID     |The UUID of the project in which the    |
|                     |*(Required)*   |share was created. Useful with          |
|                     |               |``all_tenants`` parameter.              |
+---------------------+---------------+----------------------------------------+
|is_public            |xsd:bool       |The level of visibility for the share.  |
|                     |*(Required)*   |Set to ``true`` to list only public     |
|                     |               |shares. Set to ``false`` to list only   |
|                     |               |private shares.                         |
+---------------------+---------------+----------------------------------------+
|consistency_group_id |csapi:UUID     |(Since API v2.4.) The UUID of the       |
|                     |*(Required)*   |consistency group where the share was   |
|                     |               |created.                                |
+---------------------+---------------+----------------------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |csapi:UUID *(Required)*  |The UUID of the share.   |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The share name.          |
+--------------------------+-------------------------+-------------------------+





**Example List Shares: JSON request**


.. code::

    {"shares": [{"id": "d94a8548-2079-4be0-b21c-0a887acd31ca","links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/shares/d94a8548-2079-4be0-b21c-0a887acd31ca","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/shares/d94a8548-2079-4be0-b21c-0a887acd31ca","rel": "bookmark"}],"name": "My_share"},{"id": "406ea93b-32e9-4907-a117-148b3945749f","links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/shares/406ea93b-32e9-4907-a117-148b3945749f","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/shares/406ea93b-32e9-4907-a117-148b3945749f","rel": "bookmark"}],"name": "Share1"}]}

