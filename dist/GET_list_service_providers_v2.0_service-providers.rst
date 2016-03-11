=============================================================================
List Service Providers -  OpenStack Compute API v2.1
=============================================================================

List Service Providers
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_service_providers_v2.0_service-providers.rst#request>`__
`Response <GET_list_service_providers_v2.0_service-providers.rst#response>`__

.. code-block:: javascript

    GET /v2.0/service-providers

Lists service providers and their associated service types.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|service_providers         |xsd:list *(Required)*    |A list of                |
|                          |                         |``service_provider``     |
|                          |                         |objects.                 |
+--------------------------+-------------------------+-------------------------+
|service_type              |xsd:string *(Required)*  |The service type, which  |
|                          |                         |is ``CORE``, ``DUMMY``,  |
|                          |                         |``FIREWALL``,            |
|                          |                         |``FLAVORS``,             |
|                          |                         |``L3_ROUTER_NAT``,       |
|                          |                         |``LOADBALANCER``,        |
|                          |                         |``LOADBALANCERV2``,      |
|                          |                         |``METERING``, ``QOS``,   |
|                          |                         |or ``VPN``.              |
+--------------------------+-------------------------+-------------------------+
|default                   |xsd:boolean *(Required)* |Defines whether the      |
|                          |                         |provider is the default  |
|                          |                         |for the service type. If |
|                          |                         |this value is ``true``,  |
|                          |                         |the provider is the      |
|                          |                         |default. If this value   |
|                          |                         |is ``false``, the        |
|                          |                         |provider is not the      |
|                          |                         |default.                 |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |User-facing provider     |
|                          |                         |name.                    |
+--------------------------+-------------------------+-------------------------+





**Example List Service Providers: JSON request**


.. code::

    {"service_providers": [{"service_type": "LOADBALANCER","default": true,"name": "haproxy"}]}

