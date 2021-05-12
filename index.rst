.. MH5 Robot documentation master file, created by
   sphinx-quickstart on Tue May 11 17:01:49 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. |br| raw:: html 

   <br>

MH5 Robot Documentation
=======================

This is the consolidated documentation for the MH5 Humanoid Robot (Miha).

The section ``GETTING STARTED`` will introduce the key :ref:`Design Principles` and the robot :ref:`Specifications`. This is a good start to have an understanding about the technical capabilities of the robot.

The section ``HARDWARE`` includes details about the the standard and customized hardware elements included in the construction of the robot. The information provided relates to:

.. csv-table:: Hardware
   :header: Section, Purpose
   :width: 18cm
   :widths: 25, 75

   :ref:`Actuators <TODO>`, Information about the actuators used in the robot |br| Information about the configuration of the actuators |br| A selection of features important for the usage of the robot
   :ref:`Frames <TODO>`, Details about the frames used in its construction 
   :ref:`Raspberry Pi HAT <>`, Details about the Raspberry Pi HAT with more |br| in-depth information about: |br| - the :ref:`Dynamixel Interface <SC16IS7XX dual UART driver>` |br| - the :ref:`TFT Display <ST7789 display driver>` |br| - the :ref:`Sound Interface <WM8960 sound driver>` |br| - the :ref:`IMU <>` and |br| - the :ref:`ADC <>` used to monitor the voltages
   :ref:`Hot-Swap battery circuits <>`,  used to manage the power supply from the two batteries in the feet
   :ref:`FSR Feet <>`, circuits used to provide: |br| - pressure information |br| - voltage and current information related to each of the batteries

The section ``ROS PACKAGES`` describes the setup of the `ROS Noetic <http://wiki.ros.org/noetic/>`_ version onto the MH5 main controller, including all dependencies needed for its correct functioning. After this it presents is detail the way the custom MH5 packages are designed and are supposed to be used. The packages are grouped in several repos to support better control over the installation (for example the ``mh5_hardware`` package is dependent on platform specific drivers and libraries like I2C, Serial, etc. that might not be available on a desktop platform, while the ``mh5_monitoring`` package makes extensive use of ``rqt`` plug-ins that are not installed on the robot by choice, instead being intended to be used on a remote desktop that has such support enabled):

.. csv-table:: ROS Packages
   :header: Section, Purpose
   :width: 18cm
   :widths: 25, 75

   ``mh5_robot``, Meta-package containing all the packages intended for deployment |br| on the robot: |br| - Usage of ``mh5_hardware`` :ref:`package <mh5_hardware_package>` |br| - Usage of ``mh5_controllers`` :ref:`package <mh5_controllers_package>` |br| - Usage of ``mh5_ui`` :ref:`package <mh5_ui_package>` |br| - Usage of ``mh5_vision`` :ref:`package <mh5_vision_package>`
   ``mh5_common``, Meta-package containing all the packages that can be deployed |br| both on the robot as well as on a remote desktop: |br| - Usage of ``mh5_description`` :ref:`package <mh5_description_package>` |br| - Usage of ``mh5_msgs`` :ref:`package <mh5_msgs_package>`
   ``mh5_remote``, Meta-package containing all the packages that can be deployed |br| on a remote desktop: |br| - Usage of ``mh5_monitor`` :ref:`package <mh5_monitor_package>`

Finally the section ``REFERENCE`` contains detail API reference for all packages and classes used in the MH5 ROS packages and is intended to help developers understand in more detail these packages. 

.. toctree::
   :maxdepth: 2
   :hidden:
   :name: gettingstarted
   :caption: GETTING STARTED

   docs/principles.rst
   docs/specifications.rst


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: HARDWARE

   mh5_hardware/docs/mh5_hardware.rst


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: ROS PACKAGES

   mh5_robot/docs/packages/mh5_hardware.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: REFERENCE

   mh5_robot/docs/reference/mh5_hardware_reference.rst
   mh5_robot/docs/reference/mh5_controllers_reference.rst

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
