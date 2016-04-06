
List Images
===========

`Request <GET_list_images_v2_tenant_id_images_detail.rst#request>`__
`Response <GET_list_images_v2_tenant_id_images_detail.rst#response>`__

.. rest_method:: GET /v2/{tenant_id}/images/detail

Lists images with details.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-disk-config:diskConfig |xsd:string               |Valid value is ``AUTO``  |
|                          |                         |or ``MANUAL``.           |
+--------------------------+-------------------------+-------------------------+





**Example List Images: JSON request**


.. code::

    

