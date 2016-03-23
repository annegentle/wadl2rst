=============================================================================
List Property Definitions -  OpenStack Image API v2
=============================================================================

List Property Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_property_definitions_v2_metadefs_namespaces_namespace_id_properties.rst#request>`__
`Response <GET_list_property_definitions_v2_metadefs_namespaces_namespace_id_properties.rst#response>`__

.. code-block:: javascript

    GET /v2/metadefs/namespaces/{namespace_id}/properties

Lists property definitions in a namespace.



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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|properties                |xsd:list *(Required)*    |A list of ``property``   |
|                          |                         |objects.                 |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name of the property.|
+--------------------------+-------------------------+-------------------------+
|title                     |xsd:string *(Required)*  |The title of the         |
|                          |                         |property.                |
+--------------------------+-------------------------+-------------------------+
|type                      |xsd:string *(Required)*  |The property type.       |
+--------------------------+-------------------------+-------------------------+
|enum                      |xsd:list *(Required)*    |Enumerated list of       |
|                          |                         |property values.         |
+--------------------------+-------------------------+-------------------------+
|items                     |xsd:string *(Required)*  |Schema for the items in  |
|                          |                         |an array.                |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The description of the   |
|                          |                         |property.                |
+--------------------------+-------------------------+-------------------------+
|operators                 |xsd:string *(Required)*  |Operators property       |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+
|default                   |xsd:base64Binary         |Default property         |
|                          |*(Required)*             |description.             |
+--------------------------+-------------------------+-------------------------+
|readonly                  |xsd:boolean *(Required)* |Indicates whether this   |
|                          |                         |is a read-only property. |
+--------------------------+-------------------------+-------------------------+
|minimum                   |xsd:string *(Required)*  |Minimum allowed          |
|                          |                         |numerical value.         |
+--------------------------+-------------------------+-------------------------+
|maximum                   |xsd:string *(Required)*  |Maximum allowed          |
|                          |                         |numerical value.         |
+--------------------------+-------------------------+-------------------------+
|minLength                 |xsd:string *(Required)*  |Minimum allowed string   |
|                          |                         |length.                  |
+--------------------------+-------------------------+-------------------------+
|maxLength                 |xsd:string *(Required)*  |Maximum allowed string   |
|                          |                         |length.                  |
+--------------------------+-------------------------+-------------------------+
|pattern                   |xsd:string *(Required)*  |A regular expression     |
|                          |                         |(ECMA 262) that a string |
|                          |                         |value must match.        |
+--------------------------+-------------------------+-------------------------+
|minItems                  |xsd:string *(Required)*  |Minimum length of an     |
|                          |                         |array.                   |
+--------------------------+-------------------------+-------------------------+
|maxItems                  |xsd:string *(Required)*  |Maximum length of an     |
|                          |                         |array.                   |
+--------------------------+-------------------------+-------------------------+
|uniqueItems               |xsd:string *(Required)*  |Indicates whether all    |
|                          |                         |values in the array must |
|                          |                         |be distinct.             |
+--------------------------+-------------------------+-------------------------+
|additionalItems           |xsd:string *(Required)*  |Describes extra items,   |
|                          |                         |if you use tuple typing. |
|                          |                         |If the value of          |
|                          |                         |``items`` is an array    |
|                          |                         |(tuple typing) and the   |
|                          |                         |instance is longer than  |
|                          |                         |the list of schemas in   |
|                          |                         |``items``, the           |
|                          |                         |additional items are     |
|                          |                         |described by the schema  |
|                          |                         |in this property. If     |
|                          |                         |this value is ``false``, |
|                          |                         |the instance cannot be   |
|                          |                         |longer than the list of  |
|                          |                         |schemas in ``items``. If |
|                          |                         |this value is ``true``,  |
|                          |                         |that is equivalent to    |
|                          |                         |the empty schema         |
|                          |                         |(anything goes).         |
+--------------------------+-------------------------+-------------------------+





**Example List Property Definitions: JSON request**


.. code::

    {
        "properties": {
            "hw_disk_bus": {
                "description": "Specifies the type of disk controller to attach disk devices to.",
                "enum": [
                    "scsi",
                    "virtio",
                    "uml",
                    "xen",
                    "ide",
                    "usb"
                ],
                "title": "Disk Bus",
                "type": "string"
            },
            "hw_machine_type": {
                "description": "Enables booting an ARM system using the specified machine type. By default, if an ARM image is used and its type is not specified, Compute uses vexpress-a15 (for ARMv7) or virt (for AArch64) machine types. Valid types can be viewed by using the virsh capabilities command (machine types are displayed in the machine tag).",
                "title": "Machine Type",
                "type": "string"
            },
            "hw_qemu_guest_agent": {
                "description": "It is a daemon program running inside the domain which is supposed to help management applications with executing functions which need assistance of the guest OS. For example, freezing and thawing filesystems, entering suspend. However, guest agent (GA) is not bullet proof, and hostile guest OS can send spurious replies.",
                "enum": [
                    "yes",
                    "no"
                ],
                "title": "QEMU Guest Agent",
                "type": "string"
            },
            "hw_rng_model": {
                "default": "virtio",
                "description": "Adds a random-number generator device to the image's instances. The cloud administrator can enable and control device behavior by configuring the instance's flavor. By default: The generator device is disabled. /dev/random is used as the default entropy source. To specify a physical HW RNG device, use the following option in the nova.conf file: rng_dev_path=/dev/hwrng",
                "title": "Random Number Generator Device",
                "type": "string"
            },
            "hw_scsi_model": {
                "default": "virtio-scsi",
                "description": "Enables the use of VirtIO SCSI (virtio-scsi) to provide block device access for compute instances; by default, instances use VirtIO Block (virtio-blk). VirtIO SCSI is a para-virtualized SCSI controller device that provides improved scalability and performance, and supports advanced SCSI hardware.",
                "title": "SCSI Model",
                "type": "string"
            },
            "hw_video_model": {
                "description": "The video image driver used.",
                "enum": [
                    "vga",
                    "cirrus",
                    "vmvga",
                    "xen",
                    "qxl"
                ],
                "title": "Video Model",
                "type": "string"
            },
            "hw_video_ram": {
                "description": "Maximum RAM for the video image. Used only if a hw_video:ram_max_mb value has been set in the flavor's extra_specs and that value is higher than the value set in hw_video_ram.",
                "title": "Max Video Ram",
                "type": "integer"
            },
            "hw_vif_model": {
                "description": "Specifies the model of virtual network interface device to use. The valid options depend on the configured hypervisor. KVM and QEMU: e1000, ne2k_pci, pcnet, rtl8139, and virtio. VMware: e1000, e1000e, VirtualE1000, VirtualE1000e, VirtualPCNet32, VirtualSriovEthernetCard, and VirtualVmxnet. Xen: e1000, netfront, ne2k_pci, pcnet, and rtl8139.",
                "enum": [
                    "e1000",
                    "ne2k_pci",
                    "pcnet",
                    "rtl8139",
                    "virtio",
                    "e1000",
                    "e1000e",
                    "VirtualE1000",
                    "VirtualE1000e",
                    "VirtualPCNet32",
                    "VirtualSriovEthernetCard",
                    "VirtualVmxnet",
                    "netfront",
                    "ne2k_pci"
                ],
                "title": "Virtual Network Interface",
                "type": "string"
            },
            "os_command_line": {
                "description": "The kernel command line to be used by the libvirt driver, instead of the default. For linux containers (LXC), the value is used as arguments for initialization. This key is valid only for Amazon kernel, ramdisk, or machine images (aki, ari, or ami).",
                "title": "Kernel Command Line",
                "type": "string"
            }
        }
    }
    

