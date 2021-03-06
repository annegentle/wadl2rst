.. -*- rst -*-
==================
 Hosts (os-hosts)
==================

Manages physical hosts. Some virt drivers don not support all host
functions. For more information, see `nova virt support
matrix <http://docs.openstack.org/developer/nova/support-matrix.html>`__

List Hosts
==========

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts

Lists hosts.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id







Response
--------





**Example List Hosts: JSON request**


.. literalinclude:: ../../doc/api_samples/os-hosts/hosts-list-resp.json
   :language: javascript


Enable Host
===========

.. rest_method:: PUT /v2.1/{tenant_id}/os-hosts/{host_name}

Enables or puts a host in maintenance mode.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id
  - host_name: host_name







**Example Enable Host: JSON request**


.. literalinclude:: ../../doc/api_samples/os-hosts/host-update-maintenance-req.json
   :language: javascript



Response
--------





**Example Enable Host: JSON request**


.. literalinclude:: ../../doc/api_samples/os-hosts/host-update-maintenance-resp.json
   :language: javascript


Show Host Details
=================

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}

Shows details for a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id
  - host_name: host_name







Response
--------





**Example Show Host Details: JSON request**


.. literalinclude:: ../../doc/api_samples/os-hosts/host-show-resp.json
   :language: javascript


Reboot Host
===========

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}/reboot

Reboots a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id
  - host_name: host_name







Response
--------





**Example Reboot Host: JSON request**


.. literalinclude:: ../../doc/api_samples/os-hosts/host-reboot-resp.json
   :language: javascript


Shut Down Host
==============

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}/shutdown

Shuts down a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id
  - host_name: host_name







Response
--------





**Example Shut Down Host: JSON request**


.. literalinclude:: ../../doc/api_samples/os-hosts/host-shutdown-resp.json
   :language: javascript


Start Host
==========

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}/startup

Starts a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id
  - host_name: host_name







Response
--------





**Example Start Host: JSON request**


.. literalinclude:: ../../doc/api_samples/os-hosts/host-start-resp.json
   :language: javascript


