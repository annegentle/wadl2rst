=============================================================================
Create Endpoint Template -  OpenStack Compute API v2.1
=============================================================================

Create Endpoint Template
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_endpoint_template_v2.0_os-kscatalog_endpointtemplates.rst#request>`__
`Response <POST_create_endpoint_template_v2.0_os-kscatalog_endpointtemplates.rst#response>`__

.. code-block:: javascript

    POST /v2.0/OS-KSCATALOG/endpointTemplates

Creates endpoint template.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|413                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|415                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|serviceId                 |xsd:string *(Required)*  |The service ID.          |
+--------------------------+-------------------------+-------------------------+
|X-Auth-Token              |xsd:string *(Required)*  |A valid authentication   |
|                          |                         |token for an             |
|                          |                         |administrative user.     |
+--------------------------+-------------------------+-------------------------+








**Example Create Endpoint Template: JSON request**


.. code::

    {"OS-KSCATALOG:endpointTemplate": {"id": 1,"region": "North","global": true,"type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","versionId": "1","versionInfo": "https://compute.north.public.com/v1/","versionList": "https://compute.north.public.com/","enabled": true}}


Response
^^^^^^^^^^^^^^^^^^





**Example Create Endpoint Template: JSON request**


.. code::

    {"OS-KSCATALOG:endpointTemplate": {"id": 1,"region": "North","global": true,"type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","enabled": true}}

