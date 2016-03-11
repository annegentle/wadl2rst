=============================================================================
List Extensions -  OpenStack Compute API v2.1
=============================================================================

List Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_extensions_v2_tenant_id_extensions.rst#request>`__
`Response <GET_list_extensions_v2_tenant_id_extensions.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/extensions

Lists all extensions.



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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|name            |xsd:string     |The name of the extension. For example, "Fox |
|                |*(Required)*   |In Socks."                                   |
+----------------+---------------+---------------------------------------------+
|description     |xsd:string     |The extension description.                   |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|alias           |xsd:string     |The alias for the extension. For example,    |
|                |*(Required)*   |"FOXNSOX," "os-availability-zone," "os-      |
|                |               |extended-quotas," "os-share-unmanage," or    |
|                |               |"os-used-limits."                            |
+----------------+---------------+---------------------------------------------+
|updated         |xsd:dateTime   |The date and time stamp when the extension   |
|                |*(Required)*   |was last updated. The date and time stamp    |
|                |               |format is `ISO 8601                          |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``.                         |
+----------------+---------------+---------------------------------------------+





**Example List Extensions: JSON request**


.. code::

    {"extensions": [{"alias": "os-extended-quotas","updated": "2013-06-09T00:00:00+00:00","name": "ExtendedQuotas","links": [],"description": "Extend quotas. Adds ability for admins to delete quota and optionally force the update Quota command."},{"alias": "os-quota-sets","updated": "2011-08-08T00:00:00+00:00","name": "Quotas","links": [],"description": "Quotas management support."},{"alias": "os-quota-class-sets","updated": "2012-03-12T00:00:00+00:00","name": "QuotaClasses","links": [],"description": "Quota classes management support."},{"alias": "os-share-unmanage","updated": "2015-02-17T00:00:00+00:00","name": "ShareUnmanage","links": [],"description": "Enable share unmanage operation."},{"alias": "os-types-manage","updated": "2011-08-24T00:00:00+00:00","name": "TypesManage","links": [],"description": "Types manage support."},{"alias": "share-actions","updated": "2012-08-14T00:00:00+00:00","name": "ShareActions","links": [],"description": "Enable share actions."},{"alias": "os-availability-zone","updated": "2015-07-28T00:00:00+00:00","name": "AvailabilityZones","links": [],"description": "Describe Availability Zones."},{"alias": "os-user-quotas","updated": "2013-07-18T00:00:00+00:00","name": "UserQuotas","links": [],"description": "Project user quota support."},{"alias": "os-share-type-access","updated": "2015-03-02T00:00:00Z","name": "ShareTypeAccess","links": [],"description": "share type access support."},{"alias": "os-types-extra-specs","updated": "2011-08-24T00:00:00+00:00","name": "TypesExtraSpecs","links": [],"description": "Type extra specs support."},{"alias": "os-admin-actions","updated": "2015-08-03T00:00:00+00:00","name": "AdminActions","links": [],"description": "Enable admin actions."},{"alias": "os-used-limits","updated": "2014-03-27T00:00:00+00:00","name": "UsedLimits","links": [],"description": "Provide data on limited resources that are being used."},{"alias": "os-services","updated": "2012-10-28T00:00:00-00:00","name": "Services","links": [],"description": "Services support."},{"alias": "os-share-manage","updated": "2015-02-17T00:00:00+00:00","name": "ShareManage","links": [],"description": "Allows existing share to be 'managed' by Manila."}]}

