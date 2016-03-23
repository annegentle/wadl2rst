=============================================================================
Create Image -  OpenStack Image API v1
=============================================================================

Create Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_image_v1_images.rst#request>`__
`Response <POST_create_image_v1_images.rst#response>`__

.. code-block:: javascript

    POST /v1/images

Registers a virtual machine (VM) image.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |Image Location           |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |Name for the image. Note |
|                          |                         |that the name of an      |
|                          |                         |image is not unique to   |
|                          |                         |an Image service node.   |
|                          |                         |The API cannot expect    |
|                          |                         |users to know the names  |
|                          |                         |of images that other     |
|                          |                         |users own.               |
+--------------------------+-------------------------+-------------------------+
|disk_format               |xsd:string *(Required)*  |The disk format of a VM  |
|                          |                         |image is the format of   |
|                          |                         |the underlying disk      |
|                          |                         |image. Virtual appliance |
|                          |                         |vendors have different   |
|                          |                         |formats for laying out   |
|                          |                         |the information          |
|                          |                         |contained in a VM disk   |
|                          |                         |image. You can set the   |
|                          |                         |disk format for your     |
|                          |                         |image to one of these    |
|                          |                         |values: ``aki`` An       |
|                          |                         |Amazon kernel image.     |
|                          |                         |``ami`` An Amazon        |
|                          |                         |machine image. ``ari``   |
|                          |                         |An Amazon ramdisk image. |
|                          |                         |``iso`` An archive       |
|                          |                         |format for the data      |
|                          |                         |contents of an optical   |
|                          |                         |disc, such as CDROM.     |
|                          |                         |``qcow2`` Supported by   |
|                          |                         |the QEMU emulator that   |
|                          |                         |can expand dynamically   |
|                          |                         |and supports Copy on     |
|                          |                         |Write. ``raw``           |
|                          |                         |Unstructured disk image  |
|                          |                         |format. ``vhd`` VHD disk |
|                          |                         |format, a common disk    |
|                          |                         |format used by VM        |
|                          |                         |monitors from VMWare,    |
|                          |                         |Xen, Microsoft,          |
|                          |                         |VirtualBox, and others.  |
|                          |                         |``vdi`` Supported by     |
|                          |                         |VirtualBox VM monitor    |
|                          |                         |and the QEMU emulator.   |
|                          |                         |``vmdk`` A common disk   |
|                          |                         |format that supported by |
|                          |                         |many VM monitors.        |
+--------------------------+-------------------------+-------------------------+
|container_format          |xsd:string *(Required)*  |A container format       |
|                          |                         |defines the file format  |
|                          |                         |of the file that         |
|                          |                         |contains the image and   |
|                          |                         |metadata about the       |
|                          |                         |actual VM. For a VM      |
|                          |                         |image with a ``bare``    |
|                          |                         |container format, the    |
|                          |                         |image is a blob of       |
|                          |                         |unstructured data. You   |
|                          |                         |can set the container    |
|                          |                         |format to one of these   |
|                          |                         |values: ``aki`` Amazon   |
|                          |                         |kernel image. ``ami``    |
|                          |                         |Amazon machine image.    |
|                          |                         |``ari`` Amazon ramdisk   |
|                          |                         |image. ``bare`` No       |
|                          |                         |container or metadata    |
|                          |                         |envelope for the image.  |
|                          |                         |``docker`` Docker tar    |
|                          |                         |archive of the container |
|                          |                         |filesystem. ``ova`` OVA  |
|                          |                         |container format.        |
|                          |                         |``ovf`` OVF container    |
|                          |                         |format.                  |
+--------------------------+-------------------------+-------------------------+





Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|location                  |xsd:anyURI *(Required)*  |A URI location for the   |
|                          |                         |image. ` <None>`__       |
+--------------------------+-------------------------+-------------------------+




