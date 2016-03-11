=============================================================================
Show Image Metadata For Volume -  OpenStack Compute API v2.1
=============================================================================

Show Image Metadata For Volume
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_image_metadata_for_volume_v2_tenant_id_os-vol-image-meta.rst#request>`__
`Response <GET_show_image_metadata_for_volume_v2_tenant_id_os-vol-image-meta.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/os-vol-image-meta

Shows image metadata for a volume.

When the request is made, the caller must specify a reference to an existing storage volume in the ``ref`` element. Each storage driver may interpret the existing storage volume reference differently but should accept a reference structure containing either a ``source-volume-id`` or ``source-volume-name`` element, if possible.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
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
|volume                    |xsd:string *(Required)*  |A ``volume`` object.     |
+--------------------------+-------------------------+-------------------------+
|host                      |xsd:string *(Required)*  |The OpenStack Block      |
|                          |                         |Storage host where the   |
|                          |                         |existing volume resides. |
+--------------------------+-------------------------+-------------------------+
|ref                       |xsd:string *(Required)*  |A reference to the       |
|                          |                         |existing volume. The     |
|                          |                         |internal structure of    |
|                          |                         |this reference is        |
|                          |                         |dependent on the         |
|                          |                         |implementation of the    |
|                          |                         |volume driver, see the   |
|                          |                         |specific driver's        |
|                          |                         |documentation for        |
|                          |                         |details of the required  |
|                          |                         |elements in the          |
|                          |                         |structure.               |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The volume name.         |
+--------------------------+-------------------------+-------------------------+
|availability_zone         |xsd:string *(Required)*  |The availability zone.   |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The volume description.  |
+--------------------------+-------------------------+-------------------------+
|volume_type               |xsd:string *(Required)*  |The associated volume    |
|                          |                         |type.                    |
+--------------------------+-------------------------+-------------------------+
|bootable                  |xsd:boolean *(Required)* |Enables or disables the  |
|                          |                         |bootable attribute. You  |
|                          |                         |can boot an instance     |
|                          |                         |from a bootable volume.  |
+--------------------------+-------------------------+-------------------------+
|metadata                  |xsd:string *(Required)*  |One or more metadata key |
|                          |                         |and value pairs to       |
|                          |                         |associate with the       |
|                          |                         |volume.                  |
+--------------------------+-------------------------+-------------------------+





**Example Show manage existing request: JSON**


.. code::

    {"volume": {"host": "geraint-VirtualBox","ref": {"source-volume-name": "existingLV","source-volume-id": "1234"},"name": "New Volume","availability_zone": "az2","description": "Volume imported from existingLV","volume_type": null,"bootable": "True","metadata": {"key1": "value1","key2": "value2"}}}


Response
^^^^^^^^^^^^^^^^^^





**Example Show Image Metadata For Volume: JSON request**


.. code::

    {"volume": {"status": "creating","user_id": "eae1472b5fc5496998a3d06550929e7e","attachments": [],"links": [{"href": "http://10.0.2.15:8776/v2/87c8522052ca4eed98bc672b4c1a3ddb/volumes/23cf872b-c781-4cd4-847d-5f2ec8cbd91c","rel": "self"},{"href": "http://10.0.2.15:8776/87c8522052ca4eed98bc672b4c1a3ddb/volumes/23cf872b-c781-4cd4-847d-5f2ec8cbd91c","rel": "bookmark"}],"availability_zone": "az2","bootable": "false","encrypted": "false","created_at": "2014-07-18T00:12:54.000000","description": "Volume imported from existingLV","os-vol-tenant-attr:tenant_id": "87c8522052ca4eed98bc672b4c1a3ddb","volume_type": null,"name": "New Volume","source_volid": null,"snapshot_id": null,"metadata": {"key2": "value2","key1": "value1"},"id": "23cf872b-c781-4cd4-847d-5f2ec8cbd91c","size": 0}}

