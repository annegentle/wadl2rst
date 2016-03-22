=============================================================================
Create Multiple Servers -  OpenStack Compute API v2.1
=============================================================================

Create Multiple Servers
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_multiple_servers_v2.1_tenant_id_servers.rst#request>`__
`Response <POST_create_multiple_servers_v2.1_tenant_id_servers.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers

Creates one or more servers.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |Create multiple servers  |                         |
|                          |without reservation ID   |                         |
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_groups           |xsd:string *(Required)*  |One or more security     |
|                          |                         |groups. Specify the name |
|                          |                         |of the security group in |
|                          |                         |the ``name`` attribute.  |
|                          |                         |If you omit this         |
|                          |                         |attribute, the API       |
|                          |                         |creates the server in    |
|                          |                         |the ``default`` security |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|user_data                 |xsd:string *(Required)*  |Configuration            |
|                          |                         |information or scripts   |
|                          |                         |to use upon launch. Must |
|                          |                         |be Base64 encoded.       |
+--------------------------+-------------------------+-------------------------+
|os-availability-          |xsd:string *(Required)*  |The availability zone    |
|zone:availability_zone    |                         |from which to launch the |
|                          |                         |server. When you         |
|                          |                         |provision resources, you |
|                          |                         |specify from which       |
|                          |                         |availability zone you    |
|                          |                         |want your instance to be |
|                          |                         |built. Typically, you    |
|                          |                         |use availability zones   |
|                          |                         |to arrange OpenStack     |
|                          |                         |compute hosts into       |
|                          |                         |logical groups. An       |
|                          |                         |availability zone        |
|                          |                         |provides a form of       |
|                          |                         |physical isolation and   |
|                          |                         |redundancy from other    |
|                          |                         |availability zones. For  |
|                          |                         |instance, if some racks  |
|                          |                         |in your data center are  |
|                          |                         |on a separate power      |
|                          |                         |source, you can put      |
|                          |                         |servers in those racks   |
|                          |                         |in their own             |
|                          |                         |availability zone.       |
|                          |                         |Availability zones can   |
|                          |                         |also help separate       |
|                          |                         |different classes of     |
|                          |                         |hardware. By segregating |
|                          |                         |resources into           |
|                          |                         |availability zones, you  |
|                          |                         |can ensure that your     |
|                          |                         |application resources    |
|                          |                         |are spread across        |
|                          |                         |disparate machines to    |
|                          |                         |achieve high             |
|                          |                         |availability in the      |
|                          |                         |event of hardware or     |
|                          |                         |other failure.           |
+--------------------------+-------------------------+-------------------------+
|server                    |csapi:ServerForCreate    |server.                  |
|                          |*(Required)*             |                         |
+--------------------------+-------------------------+-------------------------+
|imageRef                  |csapi:string *(Required)*|The image reference, as  |
|                          |                         |a UUID or full URL, for  |
|                          |                         |the image to use for     |
|                          |                         |your server instance.    |
+--------------------------+-------------------------+-------------------------+
|flavorRef                 |csapi:string *(Required)*|The flavor reference, as |
|                          |                         |a UUID or full URL, for  |
|                          |                         |the flavor for your      |
|                          |                         |server instance.         |
+--------------------------+-------------------------+-------------------------+
|networks                  |xsd:string *(Required)*  |A ``networks`` object.   |
|                          |                         |By default, the API      |
|                          |                         |provisions the server    |
|                          |                         |instance with all        |
|                          |                         |isolated networks for    |
|                          |                         |the tenant. Optionally,  |
|                          |                         |you can create one or    |
|                          |                         |more NICs on the server. |
|                          |                         |To provision the server  |
|                          |                         |instance with a NIC for  |
|                          |                         |a network, specify the   |
|                          |                         |UUID of the network in   |
|                          |                         |the ``uuid`` attribute   |
|                          |                         |in a ``networks``        |
|                          |                         |object. To provision the |
|                          |                         |server instance with a   |
|                          |                         |NIC for an already       |
|                          |                         |existing port, specify   |
|                          |                         |the port-id in the       |
|                          |                         |``port`` attribute in a  |
|                          |                         |``networks`` object.     |
+--------------------------+-------------------------+-------------------------+
|uuid                      |xsd:string *(Required)*  |To provision the server  |
|                          |                         |instance with a NIC for  |
|                          |                         |a network, specify the   |
|                          |                         |UUID of the network in   |
|                          |                         |the ``uuid`` attribute   |
|                          |                         |in a ``networks``        |
|                          |                         |object. Required if you  |
|                          |                         |omit the ``port``        |
|                          |                         |attribute.               |
+--------------------------+-------------------------+-------------------------+
|port                      |xsd:string *(Required)*  |To provision the server  |
|                          |                         |instance with a NIC for  |
|                          |                         |an already existing      |
|                          |                         |port, specify the port-  |
|                          |                         |id in the ``port``       |
|                          |                         |attribute in a           |
|                          |                         |``networks`` object. The |
|                          |                         |port status must be      |
|                          |                         |``DOWN``. required if    |
|                          |                         |you omit the ``uuid``    |
|                          |                         |attribute.               |
+--------------------------+-------------------------+-------------------------+
|fixed_ip                  |xsd:string *(Required)*  |A fixed IPv4 address for |
|                          |                         |the NIC. Valid with a    |
|                          |                         |``neutron`` or ``nova-   |
|                          |                         |networks`` network.      |
+--------------------------+-------------------------+-------------------------+
|name                      |csapi:string *(Required)*|The server name.         |
+--------------------------+-------------------------+-------------------------+
|metadata                  |csapi:string *(Required)*|Metadata key and value   |
|                          |                         |pairs. The maximum size  |
|                          |                         |of the metadata key and  |
|                          |                         |value is 255 bytes each. |
+--------------------------+-------------------------+-------------------------+
|personality               |csapi:string *(Required)*|The file path and        |
|                          |                         |contents, text only, to  |
|                          |                         |inject into the server   |
|                          |                         |at launch. The maximum   |
|                          |                         |size of the file path    |
|                          |                         |data is 255 bytes. The   |
|                          |                         |maximum limit is The     |
|                          |                         |number of allowed bytes  |
|                          |                         |in the decoded, rather   |
|                          |                         |than encoded, data.      |
+--------------------------+-------------------------+-------------------------+
|block_device_mapping_v2   |csapi:string *(Required)*|Enables you to boot a    |
|                          |                         |server from a volume     |
|                          |                         |when you specify         |
|                          |                         |additional parameters.   |
|                          |                         |If you specify the       |
|                          |                         |volume status, you must  |
|                          |                         |set it to ``available``. |
|                          |                         |In the OpenStack Block   |
|                          |                         |Storage database, the    |
|                          |                         |volume ``attach_status`` |
|                          |                         |must be ``detached``.    |
+--------------------------+-------------------------+-------------------------+
|device_name               |csapi:string *(Required)*|A path to the device for |
|                          |                         |the volume that you want |
|                          |                         |to use to boot the       |
|                          |                         |server.                  |
+--------------------------+-------------------------+-------------------------+
|source_type               |csapi:string *(Required)*|The source type of the   |
|                          |                         |volume. A valid value is |
|                          |                         |``blank``, ``snapshot``, |
|                          |                         |``volume``, or ``image``.|
+--------------------------+-------------------------+-------------------------+
|destination_type          |csapi:string *(Required)*|Defines where the volume |
|                          |                         |comes from. A valid      |
|                          |                         |value is ``local`` or    |
|                          |                         |``volume``.              |
+--------------------------+-------------------------+-------------------------+
|delete_on_termination     |csapi:string *(Required)*|To delete the boot       |
|                          |                         |volume when the server   |
|                          |                         |is destroyed, specify    |
|                          |                         |``true``. Otherwise,     |
|                          |                         |specify ``false``.       |
+--------------------------+-------------------------+-------------------------+
|guest_format              |csapi:string *(Required)*|Specifies the guest      |
|                          |                         |server disk file system  |
|                          |                         |format, such as          |
|                          |                         |``ephemeral`` or         |
|                          |                         |``swap``.                |
+--------------------------+-------------------------+-------------------------+
|boot_index                |csapi:string *(Required)*|Defines the order in     |
|                          |                         |which a hypervisor tries |
|                          |                         |devices when it attempts |
|                          |                         |to boot the guest from   |
|                          |                         |storage. Give each       |
|                          |                         |device a unique boot     |
|                          |                         |index starting from      |
|                          |                         |``0``. To disable a      |
|                          |                         |device from booting, set |
|                          |                         |the boot index to a      |
|                          |                         |negative value or use    |
|                          |                         |the default boot index   |
|                          |                         |value, which is          |
|                          |                         |``None``. The simplest   |
|                          |                         |usage is, set the boot   |
|                          |                         |index of the boot device |
|                          |                         |to ``0`` and use the     |
|                          |                         |default boot index       |
|                          |                         |value, ``None``, for any |
|                          |                         |other devices. Some      |
|                          |                         |hypervisors might not    |
|                          |                         |support booting from     |
|                          |                         |multiple devices; these  |
|                          |                         |hypervisors consider     |
|                          |                         |only the device with a   |
|                          |                         |boot index of ``0``.     |
|                          |                         |Some hypervisors support |
|                          |                         |booting from multiple    |
|                          |                         |devices but only if the  |
|                          |                         |devices are of different |
|                          |                         |types. For example, a    |
|                          |                         |disk and CD-ROM.         |
+--------------------------+-------------------------+-------------------------+
|config_drive              |xsd:boolean *(Required)* |Indicates whether a      |
|                          |                         |configuration drive      |
|                          |                         |enables metadata         |
|                          |                         |injection.               |
+--------------------------+-------------------------+-------------------------+
|key_name                  |xsd:string *(Required)*  |Key pair name.           |
+--------------------------+-------------------------+-------------------------+
|os:scheduler_hints        |xsd:dict *(Required)*    |The dictionary of data   |
|                          |                         |to send to the           |
|                          |                         |scheduler.               |
|                          |                         |Alternatively, you can   |
|                          |                         |specify ``OS-SCH-        |
|                          |                         |HNT:scheduler_hints`` as |
|                          |                         |the string.              |
+--------------------------+-------------------------+-------------------------+
|OS-DCF:diskConfig         |xsd:string *(Required)*  |Controls how the API     |
|                          |                         |partitions the disk when |
|                          |                         |you create, rebuild, or  |
|                          |                         |resize servers. A server |
|                          |                         |inherits the ``OS-       |
|                          |                         |DCF:diskConfig`` value   |
|                          |                         |from the image from      |
|                          |                         |which it was created,    |
|                          |                         |and an image inherits    |
|                          |                         |the ``OS-                |
|                          |                         |DCF:diskConfig`` value   |
|                          |                         |from the server from     |
|                          |                         |which it was created. To |
|                          |                         |override the inherited   |
|                          |                         |setting, you can include |
|                          |                         |this attribute in the    |
|                          |                         |request body of a server |
|                          |                         |create, rebuild, or      |
|                          |                         |resize request. If the   |
|                          |                         |``OS-DCF:diskConfig``    |
|                          |                         |value for an image is    |
|                          |                         |``MANUAL``, you cannot   |
|                          |                         |create a server from     |
|                          |                         |that image and set its   |
|                          |                         |``OS-DCF:diskConfig``    |
|                          |                         |value to ``AUTO``. A     |
|                          |                         |valid value is:          |
|                          |                         |``AUTO``. The API builds |
|                          |                         |the server with a single |
|                          |                         |partition the size of    |
|                          |                         |the target flavor disk.  |
|                          |                         |The API automatically    |
|                          |                         |adjusts the file system  |
|                          |                         |to fit the entire        |
|                          |                         |partition. ``MANUAL``.   |
|                          |                         |The API builds the       |
|                          |                         |server by using whatever |
|                          |                         |partition scheme and     |
|                          |                         |file system is in the    |
|                          |                         |source image. If the     |
|                          |                         |target flavor disk is    |
|                          |                         |larger, the API does not |
|                          |                         |partition the remaining  |
|                          |                         |disk space.              |
+--------------------------+-------------------------+-------------------------+
|return_reservation_id     |xsd:boolean *(Required)* |Set to ``True`` to       |
|                          |                         |request that the         |
|                          |                         |response return a        |
|                          |                         |reservation ID instead   |
|                          |                         |of instance information. |
|                          |                         |Default is ``False``.    |
+--------------------------+-------------------------+-------------------------+





**Example Create multiple servers without reservation ID**


.. code::

    {
        "server": {
            "name": "new-server-test",
            "imageRef": "http://openstack.example.com/openstack/images/70a599e0-31e7-49b7-b260-868f441e862b",
            "flavorRef": "http://openstack.example.com/openstack/flavors/1",
            "metadata": {
                "My Server Name": "Apache1"
            },
            "min_count": "2",
            "max_count": "3"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|server                    |xsd:dict *(Required)*    |A ``server`` object.     |
+--------------------------+-------------------------+-------------------------+
|adminPass                 |csapi:string *(Required)*|The administrative       |
|                          |                         |password of the server.  |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+
|links                     |xsd:string *(Required)*  |Server links.            |
+--------------------------+-------------------------+-------------------------+
|OS-DCF:diskConfig         |xsd:string *(Required)*  |Disk configuration. The  |
|                          |                         |value is either:         |
|                          |                         |``AUTO``. The API builds |
|                          |                         |the server with a single |
|                          |                         |partition the size of    |
|                          |                         |the target flavor disk.  |
|                          |                         |The API automatically    |
|                          |                         |adjusts the file system  |
|                          |                         |to fit the entire        |
|                          |                         |partition. ``MANUAL``.   |
|                          |                         |The API builds the       |
|                          |                         |server by using the      |
|                          |                         |partition scheme and     |
|                          |                         |file system that is in   |
|                          |                         |the source image. If the |
|                          |                         |target flavor disk is    |
|                          |                         |larger, The API does not |
|                          |                         |partition the remaining  |
|                          |                         |disk space.              |
+--------------------------+-------------------------+-------------------------+
|security_groups           |xsd:string *(Required)*  |Security groups object.  |
+--------------------------+-------------------------+-------------------------+





**Example Create multiple servers without reservation ID**


.. code::

    {
        "server": {
            "OS-DCF:diskConfig": "AUTO",
            "adminPass": "zPnp2GseTqG4",
            "id": "8195065c-fea4-4d57-b93f-5c5c63fe90e8",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/servers/8195065c-fea4-4d57-b93f-5c5c63fe90e8",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/servers/8195065c-fea4-4d57-b93f-5c5c63fe90e8",
                    "rel": "bookmark"
                }
            ],
            "security_groups": [
                {
                    "name": "default"
                }
            ]
        }
    }
    

