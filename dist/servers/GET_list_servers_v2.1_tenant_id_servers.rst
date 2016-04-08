
List Servers
============

`Request <GET_list_servers_v2.1_tenant_id_servers.rst#request>`__
`Response <GET_list_servers_v2.1_tenant_id_servers.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers

Lists IDs, names, and links for all servers.

Servers contain a status attribute that indicates the current server state. You can filter on the server status when you complete a list servers request. The server status is returned in the response body. The possible server status values are:

Server status values``ACTIVE``. The server is active.

``BUILDING``. The server has not finished the original build process.

``DELETED``. The server is permanently deleted.

``ERROR``. The server is in error.

``HARD_REBOOT``. The server is hard rebooting. This is equivalent to pulling the power plug on a physical server, plugging it back in, and rebooting it.

``MIGRATING``. The server is being migrated to a new host.

``PASSWORD``. The password is being reset on the server.

``PAUSED``. In a paused state, the state of the server is stored in RAM. A paused server continues to run in frozen state.

``REBOOT``. The server is in a soft reboot state. A reboot command was passed to the operating system.

``REBUILD``. The server is currently being rebuilt from an image.

``RESCUED``. The server is in rescue mode. A rescue image is running with the original server image attached.

``RESIZED``. Server is performing the differential copy of data that changed during its initial copy. Server is down for this stage.

``REVERT_RESIZE``. The resize or migration of a server failed for some reason. The destination server is being cleaned up and the original source server is restarting.

``SOFT_DELETED``. The server is marked as deleted but the disk images are still available to restore.

``STOPPED``. The server is powered off and the disk image still persists.

``SUSPENDED``. The server is suspended, either by request or necessity. This status appears for only the XenServer/XCP, KVM, and ESXi hypervisors. Administrative users can suspend an instance if it is infrequently used or to perform system maintenance. When you suspend an instance, its VM state is stored on disk, all memory is written to disk, and the virtual machine is stopped. Suspending an instance is similar to placing a device in hibernation; memory and vCPUs become available to create other instances.

``UNKNOWN``. The state of the server is unknown. Contact your cloud provider.

``VERIFY_RESIZE``. System is awaiting confirmation that the server is operational after a move or resize.



Normal response codes: 200,,503,400,401,403,405

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


.. rest_parameters:: listServers.yaml

	- changes-since: changes-since
	- image: image
	- flavor: flavor
	- name: name
	- status: status
	- host: host
	- limit: limit
	- marker: marker






Response
^^^^^^^^


.. rest_parameters:: listServers.yaml

	- servers: servers
	- id: id
	- links: links
	- name: name




**Example List Servers: JSON request**


.. code::

    {
        "servers": [
            {
                "id": "a291599e-6de2-41a6-88df-c443ddcef70d",
                "links": [
                    {
                        "href": "http://openstack.example.com/v2/openstack/servers/a291599e-6de2-41a6-88df-c443ddcef70d",
                        "rel": "self"
                    },
                    {
                        "href": "http://openstack.example.com/openstack/servers/a291599e-6de2-41a6-88df-c443ddcef70d",
                        "rel": "bookmark"
                    }
                ],
                "name": "new-server-test"
            }
        ]
    }
    

