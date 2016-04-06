
Create Server
=============

`Request <POST_create_server_v2.1_tenant_id_servers.rst#request>`__
`Response <POST_create_server_v2.1_tenant_id_servers.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers

Creates a server.

The progress of this operation depends on the location of the requested image, network I/O, host load, selected flavor, and other factors.

To check the progress of the request, make a ``GET /servers/{id}`` request. This call returns a progress attribute, which is a percentage value from 0 to 100.

The ``Location`` header returns the full URL to the newly created server and is available as a ``self`` and ``bookmark`` link in the server representation.

When you create a server, the response shows only the server ID, its links, and the admin password. You can get additional attributes through subsequent ``GET`` requests on the server.

Include the ``block-device-mapping-v2`` parameter in the create request body to boot a server from a volume.

Include the ``key_name`` parameter in the create request body to add a keypair to the server when you create it. To create a keypair, make a `create keypair <http://developer.openstack.org/api-ref-compute-v2.1.html#createKeypair>`__ request.

Preconditions

The user must have sufficient server quota to create the number of servers requested.

The connection to the Image service is valid.

Asynchronous postconditions

With correct permissions, you can see the server status as ``ACTIVE`` through API calls.

With correct access, you can see the created server in the compute node that OpenStack Compute manages.

Troubleshooting

If the server status remains ``BUILDING`` or shows another error status, the request failed. Ensure you meet the preconditions then investigate the compute node.

The server is not created in the compute node that OpenStack Compute manages.

The compute node needs enough free resource to match the resource of the server creation request.

Ensure that the scheduler selection filter can fulfill the request with the available compute nodes that match the selection criteria of the filter.



Normal response codes: 202,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+-----------------------+-----------------------+------------------------------+
|Name                   |Type                   |Description                   |
+=======================+=======================+==============================+
|security_groups        |xsd:list *(Required)*  |One or more security groups.  |
|                       |                       |Specify the name of the       |
|                       |                       |security group in the         |
|                       |                       |``name`` attribute. If you    |
|                       |                       |omit this attribute, the API  |
|                       |                       |creates the server in the     |
|                       |                       |``default`` security group.   |
+-----------------------+-----------------------+------------------------------+
|user_data              |xsd:string *(Required)*|Configuration information or  |
|                       |                       |scripts to use upon launch.   |
|                       |                       |Must be Base64 encoded.       |
+-----------------------+-----------------------+------------------------------+
|os-availability-       |xsd:string *(Required)*|The availability zone from    |
|zone:availability_zone |                       |which to launch the server.   |
|                       |                       |When you provision resources, |
|                       |                       |you specify from which        |
|                       |                       |availability zone you want    |
|                       |                       |your instance to be built.    |
|                       |                       |Typically, you use            |
|                       |                       |availability zones to arrange |
|                       |                       |OpenStack compute hosts into  |
|                       |                       |logical groups. An            |
|                       |                       |availability zone provides a  |
|                       |                       |form of physical isolation    |
|                       |                       |and redundancy from other     |
|                       |                       |availability zones. For       |
|                       |                       |instance, if some racks in    |
|                       |                       |your data center are on a     |
|                       |                       |separate power source, you    |
|                       |                       |can put servers in those      |
|                       |                       |racks in their own            |
|                       |                       |availability zone.            |
|                       |                       |Availability zones can also   |
|                       |                       |help separate different       |
|                       |                       |classes of hardware. By       |
|                       |                       |segregating resources into    |
|                       |                       |availability zones, you can   |
|                       |                       |ensure that your application  |
|                       |                       |resources are spread across   |
|                       |                       |disparate machines to achieve |
|                       |                       |high availability in the      |
|                       |                       |event of hardware or other    |
|                       |                       |failure.                      |
+-----------------------+-----------------------+------------------------------+
|server                 |xsd:dict *(Required)*  |server.                       |
+-----------------------+-----------------------+------------------------------+
|imageRef               |xsd:string *(Required)*|The image reference, as a     |
|                       |                       |UUID or full URL, for the     |
|                       |                       |image to use for your server  |
|                       |                       |instance.                     |
+-----------------------+-----------------------+------------------------------+
|flavorRef              |xsd:string *(Required)*|The flavor reference, as a    |
|                       |                       |UUID or full URL, for the     |
|                       |                       |flavor for your server        |
|                       |                       |instance.                     |
+-----------------------+-----------------------+------------------------------+
|networks               |xsd:string *(Required)*|A ``networks`` object.        |
|                       |                       |Required parameter when there |
|                       |                       |are mulitple networks defined |
|                       |                       |for the tenant. When you do   |
|                       |                       |not specify the networks      |
|                       |                       |parameter, the server         |
|                       |                       |attaches to the only network  |
|                       |                       |created for the current       |
|                       |                       |tenant. Optionally, you can   |
|                       |                       |create one or more NICs on    |
|                       |                       |the server. To provision the  |
|                       |                       |server instance with a NIC    |
|                       |                       |for a network, specify the    |
|                       |                       |UUID of the network in the    |
|                       |                       |``uuid`` attribute in a       |
|                       |                       |``networks`` object. To       |
|                       |                       |provision the server instance |
|                       |                       |with a NIC for an already     |
|                       |                       |existing port, specify the    |
|                       |                       |port-id in the ``port``       |
|                       |                       |attribute in a ``networks``   |
|                       |                       |object.                       |
+-----------------------+-----------------------+------------------------------+
|uuid                   |csapi:UUID *(Required)*|To provision the server       |
|                       |                       |instance with a NIC for a     |
|                       |                       |network, specify the UUID of  |
|                       |                       |the network in the ``uuid``   |
|                       |                       |attribute in a ``networks``   |
|                       |                       |object. Required if you omit  |
|                       |                       |the ``port`` attribute.       |
+-----------------------+-----------------------+------------------------------+
|port                   |xsd:string *(Required)*|To provision the server       |
|                       |                       |instance with a NIC for an    |
|                       |                       |already existing port,        |
|                       |                       |specify the port-id in the    |
|                       |                       |``port`` attribute in a       |
|                       |                       |``networks`` object. The port |
|                       |                       |status must be ``DOWN``.      |
|                       |                       |required if you omit the      |
|                       |                       |``uuid`` attribute.           |
+-----------------------+-----------------------+------------------------------+
|fixed_ip               |xsd:string *(Required)*|A fixed IPv4 address for the  |
|                       |                       |NIC. Valid with a ``neutron`` |
|                       |                       |or ``nova-networks`` network. |
+-----------------------+-----------------------+------------------------------+
|name                   |xsd:string *(Required)*|The server name.              |
+-----------------------+-----------------------+------------------------------+
|metadata               |xsd:dict *(Required)*  |Metadata key and value pairs. |
|                       |                       |The maximum size of the       |
|                       |                       |metadata key and value is 255 |
|                       |                       |bytes each.                   |
+-----------------------+-----------------------+------------------------------+
|personality            |xsd:string *(Required)*|The file path and contents,   |
|                       |                       |text only, to inject into the |
|                       |                       |server at launch. The maximum |
|                       |                       |size of the file path data is |
|                       |                       |255 bytes. The maximum limit  |
|                       |                       |is The number of allowed      |
|                       |                       |bytes in the decoded, rather  |
|                       |                       |than encoded, data.           |
+-----------------------+-----------------------+------------------------------+
|block_device_mapping_v2|xsd:dict *(Required)*  |Enables fine grained control  |
|                       |                       |of the block device mapping   |
|                       |                       |for an instance. This is      |
|                       |                       |typically used for booting    |
|                       |                       |servers from volumes. An      |
|                       |                       |example format would look as  |
|                       |                       |follows:                      |
|                       |                       |``"block_device_mapping_v2":  |
|                       |                       |{ "boot_index": "0", "uuid":  |
|                       |                       |"ac408821-c95a-448f-9292-     |
|                       |                       |73986c790911", "source_type": |
|                       |                       |"image", "volume_size": "25", |
|                       |                       |"destination_type": "volume", |
|                       |                       |"delete_on_termination": true |
|                       |                       |}``                           |
+-----------------------+-----------------------+------------------------------+
|device_name            |xsd:string *(Required)*|A path to the device for the  |
|                       |                       |volume that you want to use   |
|                       |                       |to boot the server.           |
+-----------------------+-----------------------+------------------------------+
|source_type            |xsd:string *(Required)*|The source type of the        |
|                       |                       |volume. A valid value is      |
|                       |                       |``blank``, ``snapshot``,      |
|                       |                       |``volume``, or ``image``.     |
+-----------------------+-----------------------+------------------------------+
|destination_type       |xsd:string *(Required)*|Defines where the volume      |
|                       |                       |comes from. A valid value is  |
|                       |                       |``local`` or ``volume``.      |
+-----------------------+-----------------------+------------------------------+
|delete_on_termination  |xsd:string *(Required)*|To delete the boot volume     |
|                       |                       |when the server is destroyed, |
|                       |                       |specify ``true``. Otherwise,  |
|                       |                       |specify ``false``.            |
+-----------------------+-----------------------+------------------------------+
|guest_format           |xsd:string *(Required)*|Specifies the guest server    |
|                       |                       |disk file system format, such |
|                       |                       |as ``ephemeral`` or ``swap``. |
+-----------------------+-----------------------+------------------------------+
|boot_index             |xsd:string *(Required)*|Defines the order in which a  |
|                       |                       |hypervisor tries devices when |
|                       |                       |it attempts to boot the guest |
|                       |                       |from storage. Give each       |
|                       |                       |device a unique boot index    |
|                       |                       |starting from ``0``. To       |
|                       |                       |disable a device from         |
|                       |                       |booting, set the boot index   |
|                       |                       |to a negative value or use    |
|                       |                       |the default boot index value, |
|                       |                       |which is ``None``. The        |
|                       |                       |simplest usage is, set the    |
|                       |                       |boot index of the boot device |
|                       |                       |to ``0`` and use the default  |
|                       |                       |boot index value, ``None``,   |
|                       |                       |for any other devices. Some   |
|                       |                       |hypervisors might not support |
|                       |                       |booting from multiple         |
|                       |                       |devices; these hypervisors    |
|                       |                       |consider only the device with |
|                       |                       |a boot index of ``0``. Some   |
|                       |                       |hypervisors support booting   |
|                       |                       |from multiple devices but     |
|                       |                       |only if the devices are of    |
|                       |                       |different types. For example, |
|                       |                       |a disk and CD-ROM.            |
+-----------------------+-----------------------+------------------------------+
|config_drive           |xsd:boolean            |Indicates whether a           |
|                       |*(Required)*           |configuration drive enables   |
|                       |                       |metadata injection. The       |
|                       |                       |config_drive setting provides |
|                       |                       |information about a drive     |
|                       |                       |that the instance can mount   |
|                       |                       |at boot time. The instance    |
|                       |                       |reads files from the drive to |
|                       |                       |get information that is       |
|                       |                       |normally available through    |
|                       |                       |the metadata service. This    |
|                       |                       |metadata is different from    |
|                       |                       |the user data. Not all cloud  |
|                       |                       |providers enable the          |
|                       |                       |``config_drive``. Read more   |
|                       |                       |in the OpenStackEnd User      |
|                       |                       |Guide.                        |
+-----------------------+-----------------------+------------------------------+
|key_name               |xsd:string *(Required)*|Key pair name.                |
+-----------------------+-----------------------+------------------------------+
|os:scheduler_hints     |xsd:dict *(Required)*  |The dictionary of data to     |
|                       |                       |send to the scheduler.        |
|                       |                       |Alternatively, you can        |
|                       |                       |specify ``OS-SCH-             |
|                       |                       |HNT:scheduler_hints`` as the  |
|                       |                       |string.                       |
+-----------------------+-----------------------+------------------------------+
|OS-DCF:diskConfig      |xsd:string *(Required)*|Controls how the API          |
|                       |                       |partitions the disk when you  |
|                       |                       |create, rebuild, or resize    |
|                       |                       |servers. A server inherits    |
|                       |                       |the ``OS-DCF:diskConfig``     |
|                       |                       |value from the image from     |
|                       |                       |which it was created, and an  |
|                       |                       |image inherits the ``OS-      |
|                       |                       |DCF:diskConfig`` value from   |
|                       |                       |the server from which it was  |
|                       |                       |created. To override the      |
|                       |                       |inherited setting, you can    |
|                       |                       |include this attribute in the |
|                       |                       |request body of a server      |
|                       |                       |create, rebuild, or resize    |
|                       |                       |request. If the ``OS-         |
|                       |                       |DCF:diskConfig`` value for an |
|                       |                       |image is ``MANUAL``, you      |
|                       |                       |cannot create a server from   |
|                       |                       |that image and set its ``OS-  |
|                       |                       |DCF:diskConfig`` value to     |
|                       |                       |``AUTO``. A valid value is:   |
|                       |                       |``AUTO``. The API builds the  |
|                       |                       |server with a single          |
|                       |                       |partition the size of the     |
|                       |                       |target flavor disk. The API   |
|                       |                       |automatically adjusts the     |
|                       |                       |file system to fit the entire |
|                       |                       |partition. ``MANUAL``. The    |
|                       |                       |API builds the server by      |
|                       |                       |using whatever partition      |
|                       |                       |scheme and file system is in  |
|                       |                       |the source image. If the      |
|                       |                       |target flavor disk is larger, |
|                       |                       |the API does not partition    |
|                       |                       |the remaining disk space.     |
+-----------------------+-----------------------+------------------------------+





**Example Create Server: JSON request**


.. code::

    {
        "server": {
            "name": "new-server-test",
            "imageRef": "http://glance.openstack.example.com/images/70a599e0-31e7-49b7-b260-868f441e862b",
            "flavorRef": "http://openstack.example.com/flavors/1",
            "metadata": {
                "My Server Name": "Apache1"
            }
        }
    }
    


Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|server                    |xsd:dict *(Required)*    |A ``server`` object.     |
+--------------------------+-------------------------+-------------------------+
|adminPass                 |xsd:string *(Required)*  |The administrative       |
|                          |                         |password of the server.  |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+
|links                     |xsd:list *(Required)*    |Server links.            |
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
|security_groups           |xsd:list *(Required)*    |Security groups object.  |
+--------------------------+-------------------------+-------------------------+





**Example Create Server: JSON request**


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
    

