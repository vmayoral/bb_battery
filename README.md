bb_battery
============


ROS package for the **BeagleBone** that publishes the battery state into a Topic. In order to do so, the node reads the TPS65217 register values through i2c-tools. 

**It seems that the PMIC registers can't be accessed using i2c-tools through python so a shell script `scripts/config.sh` has been created to set the desired configuration for the battery**.


----------------

This ROS package makes use of the Linux i2c-tools so you should install them before running the package

--------------
