=============================================================================
Show Server Details -  OpenStack Compute API v2.1
=============================================================================

Show Server Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_server_details_v2.1_tenant_id_servers_server_id_.rst#request>`__
`Response <GET_show_server_details_v2.1_tenant_id_servers_server_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}

Shows details for a server.

Includes server details including configuration drive, extended status, and server usage information.

The extended status information appears in the ``OS-EXT-STS:vm_state``, ``OS-EXT-STS:power_state``, and ``OS-EXT-STS:task_state`` attributes.

The server usage information appears in the ``OS-SRV-USG:launched_at`` and ``OS-SRV-USG:terminated_at`` attributes.

To hide ``addresses`` information for instances in a certain state, set the ``osapi_hide_server_address_states`` configuration option. Set this option to a valid VM state in the ``nova.conf`` configuration file.

HostId is unique peraccount and is not globally unique.

Preconditions

The server must exist.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
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
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+-------------------------+-------------+---------------------------------------------+
|Name                     |Type         |Description                                  |
+=========================+=============+=============================================+
|server                   |xsd:string   |A ``server`` object.                         |
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
|hostId                   |xsd:string   |The ID of the host.                          |
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
|links                    |xsd:string   |Server links.                                |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|metadata                 |xsd:string   |The associated metadata key and value pairs. |
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
|OS-EXT-STS:power_state   |xsd:string   |The power state of the instance.             |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-STS:task_state    |csapi:string |The task state of the instance.              |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|OS-EXT-STS:vm_state      |csapi:string |The VM state.                                |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|os-extended-             |csapi:dict   |The attached volumes, if any.                |
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
|security_groups          |xsd:string   |Security groups object.                      |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|description              |xsd:string   |The security group description.              |
|                         |*(Required)* |                                             |
+-------------------------+-------------+---------------------------------------------+
|id                       |xsd:int      |The security group ID.                       |
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
|updated                  |xsd:string   |The date and time when the resource was      |
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





**Example Show Server Details: JSON request**


.. code::

    {
        "server": {
            "addresses": {
                "private": [
                    {
                        "addr": "192.168.0.3",
                        "OS-EXT-IPS-MAC:mac_addr": "aa:bb:cc:dd:ee:ff",
                        "OS-EXT-IPS:type": "fixed",
                        "version": 4
                    }
                ]
            },
            "created": "2013-09-23T13:37:00Z",
            "flavor": {
                "id": "1",
                "links": [
                    {
                        "href": "http://openstack.example.com/openstack/flavors/1",
                        "rel": "bookmark"
                    }
                ]
            },
            "hostId": "9cc36101a27c2a69c1a18241f6228454d9d7f466bd90c62db8e8b856",
            "id": "f474386b-4fb6-4e1f-b1d5-d6bf4437f7d5",
            "image": {
                "id": "70a599e0-31e7-49b7-b260-868f441e862b",
                "links": [
                    {
                        "href": "http://openstack.example.com/openstack/images/70a599e0-31e7-49b7-b260-868f441e862b",
                        "rel": "bookmark"
                    }
                ]
            },
            "key_name": null,
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/servers/f474386b-4fb6-4e1f-b1d5-d6bf4437f7d5",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/servers/f474386b-4fb6-4e1f-b1d5-d6bf4437f7d5",
                    "rel": "bookmark"
                }
            ],
            "metadata": {
                "My Server Name": "Apache1"
            },
            "name": "new-server-test",
            "accessIPv4": "192.0.2.0",
            "accessIPv6": "2002:0:0:0:0:0:c000:20e",
            "config_drive": "",
            "OS-DCF:diskConfig": "AUTO",
            "OS-EXT-AZ:availability_zone": "nova",
            "OS-EXT-SRV-ATTR:host": "b8b357f7100d4391828f2177c922ef93",
            "OS-EXT-SRV-ATTR:hypervisor_hostname": "fake-mini",
            "OS-EXT-SRV-ATTR:instance_name": "instance-00000001",
            "OS-EXT-STS:power_state": 1,
            "OS-EXT-STS:task_state": null,
            "OS-EXT-STS:vm_state": "active",
            "os-extended-volumes:volumes_attached": [],
            "OS-SRV-USG:launched_at": "2013-09-23T13:37:00.880302",
            "OS-SRV-USG:terminated_at": null,
            "progress": 0,
            "security_groups": [
                {
                    "name": "default"
                }
            ],
            "status": "ACTIVE",
            "host_status": "UP",
            "tenant_id": "openstack",
            "updated": "2013-10-31T07:31:30Z",
            "user_id": "fake"
        }
    }
    

