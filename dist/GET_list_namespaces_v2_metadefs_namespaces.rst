=============================================================================
List Namespaces -  OpenStack Compute API v2.1
=============================================================================

List Namespaces
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_namespaces_v2_metadefs_namespaces.rst#request>`__
`Response <GET_list_namespaces_v2_metadefs_namespaces.rst#response>`__

.. code-block:: javascript

    GET /v2/metadefs/namespaces

Lists public namespaces.

Returns a subset in the larger collection of namespaces and a link that you can use to get the next set of namespaces. Check for the presence of a ``next`` link and use it as the URI in a subsequent HTTP GET request. Follow this pattern until a ``next`` link is no longer provided. The ``next`` link preserves any query parameters that you send in your initial request. You can use the ``first`` link to return to the first page in the collection. If you prefer to paginate through namespaces manually, use the ``limit`` and ``marker`` parameters.

The list operation accepts the ``resource_types`` and ``visibility`` query parameters, which you can use to filter the response.

To sort the results of this operation, use the ``sort_key`` and ``sort_dir`` parameters. The API uses the natural sorting order in the namespace attribute that you provide as the ``sort_key`` parameter.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^




This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|limit                     |xsd:int *(Required)*     |Requests a page size of  |
|                          |                         |items. Returns a number  |
|                          |                         |of items up to a limit   |
|                          |                         |value. Use the ``limit`` |
|                          |                         |parameter to make an     |
|                          |                         |initial limited request  |
|                          |                         |and use the ID of the    |
|                          |                         |last-seen item from the  |
|                          |                         |response as the          |
|                          |                         |``marker`` parameter     |
|                          |                         |value in a subsequent    |
|                          |                         |limited request.         |
+--------------------------+-------------------------+-------------------------+
|marker                    |xsd:string *(Required)*  |The ID of the last-seen  |
|                          |                         |item. Use the ``limit``  |
|                          |                         |parameter to make an     |
|                          |                         |initial limited request  |
|                          |                         |and use the ID of the    |
|                          |                         |last-seen item from the  |
|                          |                         |response as the          |
|                          |                         |``marker`` parameter     |
|                          |                         |value in a subsequent    |
|                          |                         |limited request.         |
+--------------------------+-------------------------+-------------------------+
|visibility                |imageapi:string          |Filters the response by  |
|                          |*(Required)*             |an image visibility      |
|                          |                         |value or values. Use the |
|                          |                         |comma ( ``,`` )          |
|                          |                         |character to separate    |
|                          |                         |multiple values. A valid |
|                          |                         |value is ``public``,     |
|                          |                         |``private``, or          |
|                          |                         |``shared``. If you omit  |
|                          |                         |this parameter, the      |
|                          |                         |response shows           |
|                          |                         |``public``, ``private``, |
|                          |                         |and ``shared`` images    |
|                          |                         |with a member status of  |
|                          |                         |``accepted``.            |
+--------------------------+-------------------------+-------------------------+
|resource_types            |xsd:int *(Required)*     |Filters the response by  |
|                          |                         |a resource type or       |
|                          |                         |types. Use the comma (   |
|                          |                         |``,`` ) character to     |
|                          |                         |separate multiple        |
|                          |                         |values. For example,     |
|                          |                         |``OS::Glance::Image,     |
|                          |                         |OS::Nova::Flavor`` shows |
|                          |                         |only namespaces for      |
|                          |                         |these resource types.    |
+--------------------------+-------------------------+-------------------------+
|sort_key                  |xsd:string *(Required)*  |Sorts the response by an |
|                          |                         |attribute, such as       |
|                          |                         |``name``, ``id``, or     |
|                          |                         |``updated_at``. Default  |
|                          |                         |is ``created_at``. The   |
|                          |                         |API uses the natural     |
|                          |                         |sorting direction of the |
|                          |                         |``sort_key`` image       |
|                          |                         |attribute.               |
+--------------------------+-------------------------+-------------------------+
|sort_dir                  |xsd:string *(Required)*  |Sorts the response by a  |
|                          |                         |set of one or more sort  |
|                          |                         |direction and attribute  |
|                          |                         |( ``sort_key`` )         |
|                          |                         |combinations. A valid    |
|                          |                         |value for the sort       |
|                          |                         |direction is ``asc``     |
|                          |                         |(ascending) or ``desc``  |
|                          |                         |(descending). If you     |
|                          |                         |omit the sort direction  |
|                          |                         |in a set, the default is |
|                          |                         |``desc``.                |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+---------------------------+-------------------------+------------------------+
|Name                       |Type                     |Description             |
+===========================+=========================+========================+
|namespaces                 |xsd:list *(Required)*    |A list of ``namespace`` |
|                           |                         |objects.                |
+---------------------------+-------------------------+------------------------+
|namespace                  |xsd:string *(Required)*  |The namespace is unique |
|                           |                         |across all users.       |
+---------------------------+-------------------------+------------------------+
|display_name               |xsd:string *(Required)*  |User-friendly name to   |
|                           |                         |use in a UI to display  |
|                           |                         |the namespace name.     |
+---------------------------+-------------------------+------------------------+
|description                |xsd:string *(Required)*  |The description of the  |
|                           |                         |namespace.              |
+---------------------------+-------------------------+------------------------+
|visibility                 |xsd:string *(Required)*  |The namespace           |
|                           |                         |visibility. A valid     |
|                           |                         |value is ``public`` or  |
|                           |                         |``private``. Default is |
|                           |                         |``private``.            |
+---------------------------+-------------------------+------------------------+
|protected                  |xsd:string *(Required)*  |Namespace protection    |
|                           |                         |for deletion. A valid   |
|                           |                         |value is ``True`` or    |
|                           |                         |``False``. Default is   |
|                           |                         |``False``.              |
+---------------------------+-------------------------+------------------------+
|resource_type_associations |xsd:string *(Required)*  |One or more namespace   |
|                           |                         |resource types.         |
+---------------------------+-------------------------+------------------------+





**Example List Namespaces: JSON request**


.. code::

    {"first": "/v2/metadefs/namespaces?sort_key=created_at&sort_dir=asc","namespaces": [{"created_at": "2014-08-28T17:13:06Z","description": "The libvirt compute driver options. These are properties specific to compute drivers.  For a list of all hypervisors, see here: https://wiki.openstack.org/wiki/HypervisorSupportMatrix.","display_name": "libvirt Driver Options","namespace": "OS::Compute::Libvirt","owner": "admin","protected": true,"resource_type_associations": [{"created_at": "2014-08-28T17:13:06Z","name": "OS::Glance::Image","updated_at": "2014-08-28T17:13:06Z"}],"schema": "/v2/schemas/metadefs/namespace","self": "/v2/metadefs/namespaces/OS::Compute::Libvirt","updated_at": "2014-08-28T17:13:06Z","visibility": "public"},{"created_at": "2014-08-28T17:13:06Z","description": "Compute drivers may enable quotas on CPUs available to a VM, disk tuning, bandwidth I/O, and instance VIF traffic control.  See: http://docs.openstack.org/admin-guide-cloud/compute-flavors.html","display_name": "Flavor Quota","namespace": "OS::Compute::Quota","owner": "admin","protected": true,"resource_type_associations": [{"created_at": "2014-08-28T17:13:06Z","name": "OS::Nova::Flavor","updated_at": "2014-08-28T17:13:06Z"}],"schema": "/v2/schemas/metadefs/namespace","self": "/v2/metadefs/namespaces/OS::Compute::Quota","updated_at": "2014-08-28T17:13:06Z","visibility": "public"},{"created_at": "2014-08-28T17:13:06Z","description": "Trusted compute pools with Intel\u00ae Trusted Execution Technology (Intel\u00ae TXT) support IT compliance by protecting virtualized data centers - private, public, and hybrid clouds against attacks toward hypervisor and BIOS, firmware, and other pre-launch software components.","display_name": "Trusted Compute Pools (Intel\u00ae TXT)","namespace": "OS::Compute::Trust","owner": "admin","protected": true,"resource_type_associations": [{"created_at": "2014-08-28T17:13:06Z","name": "OS::Nova::Flavor","updated_at": "2014-08-28T17:13:06Z"}],"schema": "/v2/schemas/metadefs/namespace","self": "/v2/metadefs/namespaces/OS::Compute::Trust","updated_at": "2014-08-28T17:13:06Z","visibility": "public"},{"created_at": "2014-08-28T17:13:06Z","description": "This provides the preferred socket/core/thread counts for the virtual CPU instance exposed to guests. This enables the ability to avoid hitting limitations on vCPU topologies that OS vendors place on their products. See also: http://git.openstack.org/cgit/openstack/nova-specs/tree/specs/juno/virt-driver-vcpu-topology.rst","display_name": "Virtual CPU Topology","namespace": "OS::Compute::VirtCPUTopology","owner": "admin","protected": true,"resource_type_associations": [{"created_at": "2014-08-28T17:13:06Z","name": "OS::Glance::Image","prefix": "hw_","updated_at": "2014-08-28T17:13:06Z"},{"created_at": "2014-08-28T17:13:06Z","name": "OS::Cinder::Volume","prefix": "hw_","properties_target": "image","updated_at": "2014-08-28T17:13:06Z"},{"created_at": "2014-08-28T17:13:06Z","name": "OS::Nova::Flavor","prefix": "hw:","updated_at": "2014-08-28T17:13:06Z"}],"schema": "/v2/schemas/metadefs/namespace","self": "/v2/metadefs/namespaces/OS::Compute::VirtCPUTopology","updated_at": "2014-08-28T17:13:06Z","visibility": "public"}],"schema": "/v2/schemas/metadefs/namespaces"}

