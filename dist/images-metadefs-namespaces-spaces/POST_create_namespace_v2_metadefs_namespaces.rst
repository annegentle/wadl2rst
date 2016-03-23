=============================================================================
Create Namespace -  OpenStack Image API v2
=============================================================================

Create Namespace
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_namespace_v2_metadefs_namespaces.rst#request>`__
`Response <POST_create_namespace_v2_metadefs_namespaces.rst#response>`__

.. code-block:: javascript

    POST /v2/metadefs/namespaces

Creates a namespace.

The ``Location`` response header contains the newly-created URI for the namespace.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









**Example Create Namespace: JSON request**


.. code::

    {
        "description": "Choose capabilities that should be provided by the Compute Host. This provides the ability to fine tune the hardware specification required when a new vm is requested.",
        "display_name": "Hypervisor Selection",
        "namespace": "OS::Compute::Hypervisor",
        "properties": {
            "hypervisor_type": {
                "description": "The hypervisor type.",
                "enum": [
                    "xen",
                    "qemu",
                    "kvm",
                    "lxc",
                    "uml",
                    "vmware",
                    "hyperv"
                ],
                "title": "Hypervisor Type",
                "type": "string"
            },
            "vm_mode": {
                "description": "The virtual machine mode.",
                "enum": [
                    "hvm",
                    "xen",
                    "uml",
                    "exe"
                ],
                "title": "VM Mode",
                "type": "string"
            }
        },
        "protected": true,
        "resource_type_associations": [
            {
                "name": "OS::Glance::Image"
            }
        ],
        "visibility": "public"
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+---------------------------+-------------------------+------------------------+
|Name                       |Type                     |Description             |
+===========================+=========================+========================+
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
|properties                 |xsd:dict *(Required)*    |One or more property    |
|                           |                         |definitions for the     |
|                           |                         |namespace.              |
+---------------------------+-------------------------+------------------------+
|objects                    |xsd:string *(Required)*  |One or more object      |
|                           |                         |definitions of the      |
|                           |                         |namespace.              |
+---------------------------+-------------------------+------------------------+
|resource_type_associations |xsd:string *(Required)*  |One or more namespace   |
|                           |                         |resource types.         |
+---------------------------+-------------------------+------------------------+
|hypervisor_type            |xsd:dict *(Required)*    |Hypervisor type of      |
|                           |                         |property values.        |
+---------------------------+-------------------------+------------------------+
|enum                       |xsd:list *(Required)*    |Enumerated list of      |
|                           |                         |property values.        |
+---------------------------+-------------------------+------------------------+





**Example Create Namespace: JSON request**


.. code::

    {
        "description": "Choose capabilities that should be provided by the Compute Host. This provides the ability to fine tune the hardware specification required when a new vm is requested.",
        "display_name": "Hypervisor Selection",
        "namespace": "OS::Compute::Hypervisor",
        "properties": {
            "hypervisor_type": {
                "description": "The hypervisor type.",
                "enum": [
                    "xen",
                    "qemu",
                    "kvm",
                    "lxc",
                    "uml",
                    "vmware",
                    "hyperv"
                ],
                "title": "Hypervisor Type",
                "type": "string"
            },
            "vm_mode": {
                "description": "The virtual machine mode.",
                "enum": [
                    "hvm",
                    "xen",
                    "uml",
                    "exe"
                ],
                "title": "VM Mode",
                "type": "string"
            }
        },
        "protected": true,
        "resource_type_associations": [
            {
                "name": "OS::Glance::Image"
            }
        ],
        "schema": "/v2/schemas/metadefs/namespace",
        "self": "/v2/metadefs/namespaces/OS::Compute::Hypervisor",
        "visibility": "public"
    }
    

