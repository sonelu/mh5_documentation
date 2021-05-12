Specifications
==============

Rev D.1 (March 2021)

Dimensions
----------

.. |br| raw:: html 

    <br>

.. csv-table:: Dimensions
    :header: Parameter, Value, Comments
    :width: 18cm
    :widths: 25, 25, 50

    Height, 48cm
    Width, 51cm, with arms stretched
    Depth, 20cm
    Weight, 2.15Kg, Including batteries
    Weight, 1.84Kg, Excluding the batteries

Actuators
---------

.. csv-table:: Actuators
    :header: Parameter, Value, Comments
    :width: 18cm
    :widths: 25, 25, 50

    Total DoF, 22
    Legs DoF (each),6, "ankle pitch and roll, |br| knee yaw and pitch, |br| hip pitch and roll"
    Legs Actuators, 6 x 2XL430, each leg contains 3 `2XL430-W250 <https://emanual.robotis.com/docs/en/dxl/x/2xl430-w250/>`_
    Arms Dof (each),4, "shoulder pitch and roll, |br| elbow yaw and pitch"
    Arms Actuators, 8 x XL430, each arm contains 4 `XL430-W250 <https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/>`_
    Head DoF, 2, pitch and yaw
    Head Actuators, 1 x 2XL430, one `2XL430-W250`_

Power
-----

.. csv-table:: Power
    :header: Parameter, Value, Comments
    :width: 18cm
    :widths: 25, 25, 50

    Batteries, 2 x 2500mAh, "3S LiPo batteries, |br| Batteries are located in the feet |br| and are hot-swap; |br| there is no need to turn off the main |br| controller to change the batteries"
    External power,	2.5mm power jack |br| 12V, Optionally the robot can be powered with |br| a 12V power adapter using a standard |br| 2.5mm barrel jack
    Autonomy, 3 hours, (preliminary estimates)
    Monitoring, voltage	ADC, "Dynamixel voltage, |br| 5V railing, |br| 3.3V railing"

Electronics
-----------

.. csv-table:: Electronics
    :header: Parameter, Value, Comments
    :width: 18cm
    :widths: 25, 25, 50

    Main controller, Raspberry Pi, Model 4 4GB RAM	
    Add on board,	Robotics HAT, "The board includes: |br| 1. dual high speed dual Dynamixel bus |br| 2. IMU (Gyroscope and Accelerometer) |br| 3. 5V 3A power switch for RPi |br| 4. ADC for monitoring power |br| 5. stereo codec with mics and 2 x 1W output |br| 6. PWM fan control |br| 7. USB to UART converter for console access"
    Hot-swap circuits, 2, "Each foot includes a circuit that implements: |br| 1. an ideal diode and allows hot-swap |br| 2. low-voltage alarm |br| 3. emergency shutdown for ultra-low voltage"
    Display, Adafruit 2.0" |br| IPS display, A 2.0'' 320x 240 IPS TFT display connected |br| on SPI with console support
    Camera, 2, Model HBV-1716HD	|br| Max resolution 1920 x 1080 |br| USB connected directly to Raspberry Pi |br| field of view 60 degrees
    WiFi, 2, Built-in 5Ghz frequency WiFi |br| Second USB dongle |br| Low-latency (5GHz band) Access Point (AP) |br| The second WiFi can connect to an exiting |br| infrastructure |br| DHCP and ip routing
    Bluetooth, Builtin, Bluetooth 5.0 BLE |br| Bluetooth keyboard for remote control |br| and interface navigation

Software
--------

.. csv-table:: Software
    :header: Parameter, Value, Comments
    :width: 18cm
    :widths: 25, 25, 50

    OS, Raspbian |br| (Debian Buster), Using Linux kernel 5.10 |br| Kernel drivers added for: |br| - SC16IS762 (SPI to UART) |br| - ST7789V (TFT display) |br| - WM8960 (sound) |br| - ADS1015 (for voltage monitoring ADC) |br|  - fan_control
    Software, ROS Noetic, ROS Noetic is installed from source
    Custom ROS packages, , The following packages are included: |br| - hardware interface |br| - controllers |br| - UI for robot TFT |br| - URDF with support for RViz and Gazebo |br| - "director" package for scripted moves |br| - vision (in progress)

Future plans
------------

There are a number of exciting upgrades to the platform that we expect to deliver soon:

.. csv-table:: Planed improvements
    :header: Area, Improvement
    :width: 18cm
    :widths: 25, 75

    Vision, Updated cameras with 100 degrees FoV and more fps options
    Foot Sensor, Soles with 4 force sensing resistors (FSR) |br| Information is exchanged over the Dynamixel bus.
    Display	, increase size of display to 2.8 inch to improve readability