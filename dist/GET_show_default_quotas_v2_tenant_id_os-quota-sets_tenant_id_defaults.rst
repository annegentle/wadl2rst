=============================================================================
Show Default Quotas -  OpenStack Compute API v2.1
=============================================================================

Show Default Quotas
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_default_quotas_v2_tenant_id_os-quota-sets_tenant_id_defaults.rst#request>`__
`Response <GET_show_default_quotas_v2_tenant_id_os-quota-sets_tenant_id_defaults.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/os-quota-sets/{tenant_id}/defaults

Shows default quotas for a tenant.



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
|{tenant_id}               |csapi:UUID *(Required)*  |The UUID for the tenant  |
|                          |                         |for which you want to    |
|                          |                         |show, update, or delete  |
|                          |                         |quotas. This ID is       |
|                          |                         |different from the first |
|                          |                         |tenant ID that you       |
|                          |                         |specify in the URI: That |
|                          |                         |ID is for the            |
|                          |                         |administrative tenant.   |
+--------------------------+-------------------------+-------------------------+
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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |for which you manage     |
|                          |                         |quotas.                  |
+--------------------------+-------------------------+-------------------------+
|gigabytes                 |xsd:int *(Required)*     |The number of gigabytes  |
|                          |                         |allowed for each tenant. |
+--------------------------+-------------------------+-------------------------+
|snapshots                 |xsd:int *(Required)*     |The number of snapshots  |
|                          |                         |allowed for each tenant. |
+--------------------------+-------------------------+-------------------------+
|shares                    |xsd:int *(Required)*     |The number of shares     |
|                          |                         |allowed for each tenant. |
+--------------------------+-------------------------+-------------------------+
|snapshot_gigabytes        |xsd:int *(Required)*     |The number of gigabytes  |
|                          |                         |for the snapshots        |
|                          |                         |allowed for each tenant. |
+--------------------------+-------------------------+-------------------------+
|share_networks            |xsd:int *(Required)*     |The number of share      |
|                          |                         |networks allowed for     |
|                          |                         |each tenant.             |
+--------------------------+-------------------------+-------------------------+





**Example Show Default Quotas: JSON request**


.. code::

    {"quota_set": {"gigabytes": 1000,"shares": 50,"snapshot_gigabytes": 1000,"snapshots": 50,"id": "16e1ab15c35a457e9c2b2aa189f544e1","share_networks": 10}}

