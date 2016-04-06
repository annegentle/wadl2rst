
Update Server
=============

`Request <PUT_update_server_v2.1_tenant_id_servers_server_id_.rst#request>`__
`Response <PUT_update_server_v2.1_tenant_id_servers_server_id_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/servers/{server_id}

Updates the editable attributes of a server.

Preconditions

The server must exist.

You can edit the ``accessIPv4``, ``accessIPv6``, ``diskConfig`` and ``name`` attributes.



Normal response codes: 200,,503,400,401,403,405,404,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id




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





**Example Update server name: JSON request**


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
    


**Example Update server IP addresses: JSON request**


.. code::

    {
        "server": {
            "accessIPv4": "192.0.2.0",
            "accessIPv6": "2002:0:0:0:0:0:c000:20e"
        }
    }
    


**Example Update server OS-DCF:diskConfig parameter: JSON request**


.. code::

    {
        "server": {
            "OS-DCF:diskConfig": "AUTO"
        }
    }
    


Response
^^^^^^^^


This table shows the body parameters for the response:

+-------------------------+-------------+---------------------------------------------+
|Name                     |Type         |Description                                  |
+=========================+=============+=============================================+
|server                   |xsd:dict     |A ``server`` object.                         |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|addresses                |xsd:dict     |The addresses for the server. Addresses      |
|                         |*(Required)* |information is hidden for any server in a    |
|                         |             |state set in the                             |
|                         |             |``osapi_hide_server_address_states``         |
|                         |             |configuration option. By default, servers in |
|                         |             |``building`` state hide their addresses      |
|                         |             |information. See `nova.conf -configuration   |
|                         |             |options                                      |
|                         |             |<http://docs.openstack.org/liberty/config-   |
|                         |             |reference/content/list-of-compute-config-    |
|                         |             |options.html>`__.                            |
+-------------------------+-------------+---------------------------------------------+
|created                  |xsd:dateTime |The date and time when the resource was      |
|                         |*(Required)* |created. The date and time stamp format is   |
|                         |             |`ISO 8601                                    |
|                         |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                         |             |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                         |             |``2015-08-27T09:49:58-05:00``. The           |
|                         |             |``±hh:mm`` value, if included, is the time   |
|                         |             |zone as an offset from UTC. In the previous  |
|                         |             |example, the offset value is ``-05:00``.     |
+-------------------------+-------------+---------------------------------------------+
|flavor                   |xsd:dict     |The ID and links for the flavor for your     |
|                         |*(Required)* |server instance. A flavor is a combination   |
|                         |             |of memory, disk size, and CPUs.              |
+-------------------------+-------------+---------------------------------------------+
|hostId                   |csapi:UUID   |The ID of the host.                          |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|id                       |csapi:UUID   |The UUID of the server.                      |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|image                    |xsd:dict     |The UUID and links for the image for your    |
|                         |*(Required)* |server instance. The ``image`` object might  |
|                         |             |be an empty string when you boot the server  |
|                         |             |from a volume.                               |
+-------------------------+-------------+---------------------------------------------+
|key_name                 |xsd:string   |The name of associated key pair, if any.     |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|links                    |xsd:list     |Server links.                                |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|metadata                 |xsd:dict     |The associated metadata key and value pairs. |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|name                     |csapi:string |The server name. The user sets the server    |
|                         |*(Required)* |name.                                        |
+-------------------------+-------------+---------------------------------------------+
|OS-DCF:diskConfig        |xsd:string   |Disk configuration. The value is either:     |
|                         |*(Required)* |``AUTO``. The API builds the server with a   |
|                         |             |single partition the size of the target      |
|                         |             |flavor disk. The API automatically adjusts   |
|                         |             |the file system to fit the entire partition. |
|                         |             |``MANUAL``. The API builds the server by     |
|                         |             |using the partition scheme and file system   |
|                         |             |that is in the source image. If the target   |
|                         |             |flavor disk is larger, The API does not      |
|                         |             |partition the remaining disk space.          |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-                  |csapi:string |The availability zone.                       |
|AZ:availability_zone     |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-SRV-ATTR:host     |csapi:string |The host name. Appears in the response for   |
|                         |*(Required)* |administrative users only.                   |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-SRV-              |csapi:string |The hypervisor host name. Appears in the     |
|ATTR:hypervisor_hostname |*(Required)* |response for administrative users only.      |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-SRV-              |csapi:string |The instance name. The Compute API generates |
|ATTR:instance_name       |*(Required)* |the instance name from the instance name     |
|                         |             |template. Appears in the response for        |
|                         |             |administrative users only.                   |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-STS:power_state   |xsd:int      |The power state of the instance.             |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-STS:task_state    |csapi:string |The task state of the instance.              |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-STS:vm_state      |csapi:string |The VM state.                                |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|os-extended-             |xsd:list     |The attached volumes, if any.                |
|volumes:volumes_attached |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|OS-SRV-USG:launched_at   |xsd:dateTime |The date and time when the server was        |
|                         |*(Required)* |launched. The date and time stamp format is  |
|                         |             |`ISO 8601                                    |
|                         |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                         |             |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                         |             |``2015-08-27T09:49:58-05:00``. The           |
|                         |             |``±hh:mm`` value, if included, is the time   |
|                         |             |zone as an offset from UTC. If the           |
|                         |             |``deleted_at`` date and time stamp is not    |
|                         |             |set, its value is ``null``.                  |
+-------------------------+-------------+---------------------------------------------+
|OS-SRV-USG:terminated_at |xsd:dateTime |The date and time when the server was        |
|                         |*(Required)* |deleted. The date and time stamp format is   |
|                         |             |`ISO 8601                                    |
|                         |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                         |             |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                         |             |``2015-08-27T09:49:58-05:00``. The           |
|                         |             |``±hh:mm`` value, if included, is the time   |
|                         |             |zone as an offset from UTC. If the           |
|                         |             |``deleted_at`` date and time stamp is not    |
|                         |             |set, its value is ``null``.                  |
+-------------------------+-------------+---------------------------------------------+
|progress                 |xsd:int      |A percentage value of the build progress.    |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|security_groups          |xsd:list     |Security groups object.                      |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|description              |xsd:string   |The security group description.              |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|id                       |csapi:UUID   |The security group ID.                       |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|name                     |xsd:string   |The security group name.                     |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|rules                    |xsd:string   |A rules object.                              |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|status                   |xsd:string   |The server status.                           |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|host_status              |xsd:string   |The host status. Values where next value in  |
|                         |*(Required)* |list can override the previous: ``UP`` if    |
|                         |             |nova-compute up. ``UNKNOWN`` if nova-compute |
|                         |             |not reported by servicegroup driver.         |
|                         |             |``DOWN`` if nova-compute forced down.        |
|                         |             |``MAINTENANCE`` if nova-compute is disabled. |
|                         |             |Empty string indicates there is no host for  |
|                         |             |server. This attribute appears in the        |
|                         |             |response only if the policy permits.         |
+-------------------------+-------------+---------------------------------------------+
|tenant_id                |csapi:UUID   |The UUID of the tenant in a multi-tenancy    |
|                         |*(Required)* |cloud.                                       |
+-------------------------+-------------+---------------------------------------------+
|updated                  |xsd:dateTime |The date and time when the resource was      |
|                         |*(Required)* |updated. The date and time stamp format is   |
|                         |             |`ISO 8601                                    |
|                         |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                         |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                         |             |value, if included, is the time zone as an   |
|                         |             |offset from UTC. For example, ``2015-08-     |
|                         |             |27T09:49:58-05:00``. The UTC time zone is    |
|                         |             |assumed.                                     |
+-------------------------+-------------+---------------------------------------------+
|user_id                  |xsd:string   |The user ID of the user who owns the server. |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+





**Example Update server name: JSON response**


.. code::

    {
        "server": {
            "id": "52415800-8b69-11e0-9b19-734f565bc83b",
            "tenant_id": "1234",
            "user_id": "5678",
            "name": "new-server-test",
            "created": "2010-11-11T12:00:00Z",
            "updated": "2010-11-12T12:44:44Z",
            "hostId": "e4d909c290d0fb1ca068ffaddf22cbd0",
            "accessIPv4": "192.0.2.0",
            "accessIPv6": "2002:0:0:0:0:0:c000:20e",
            "progress": 0,
            "status": "ACTIVE",
            "image": {
                "id": "52415800-8b69-11e0-9b19-734f6f006e54",
                "name": "CentOS 5.2",
                "links": [
                    {
                        "rel": "self",
                        "href": "http://servers.api.openstack.org/v2/1234/images/52415800-8b69-11e0-9b19-734f6f006e54"
                    },
                    {
                        "rel": "bookmark",
                        "href": "http://servers.api.openstack.org/1234/images/52415800-8b69-11e0-9b19-734f6f006e54"
                    }
                ]
            },
            "flavor": {
                "id": "52415800-8b69-11e0-9b19-734f1195ff37",
                "name": "256 MB Server",
                "links": [
                    {
                        "rel": "self",
                        "href": "http://servers.api.openstack.org/v2/1234/flavors/52415800-8b69-11e0-9b19-734f1195ff37"
                    },
                    {
                        "rel": "bookmark",
                        "href": "http://servers.api.openstack.org/1234/flavors/52415800-8b69-11e0-9b19-734f1195ff37"
                    }
                ]
            },
            "metadata": {
                "My Server Name": "Apache1"
            },
            "addresses": {
                "public": [
                    {
                        "version": 4,
                        "addr": "192.0.2.0"
                    },
                    {
                        "version": 6,
                        "addr": "2002:0:0:0:0:0:c000:20e"
                    }
                ],
                "private": [
                    {
                        "version": 4,
                        "addr": "198.51.100.0"
                    },
                    {
                        "version": 6,
                        "addr": "2002:0:0:0:0:0:c633:640e"
                    }
                ]
            },
            "links": [
                {
                    "rel": "self",
                    "href": "http://servers.api.openstack.org/v2/1234/servers/52415800-8b69-11e0-9b19-734fcece0043"
                },
                {
                    "rel": "bookmark",
                    "href": "http://servers.api.openstack.org/1234/servers/52415800-8b69-11e0-9b19-734fcece0043"
                }
            ]
        }
    }
    

