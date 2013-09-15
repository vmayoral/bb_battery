#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import subprocess
import os
from i2ctools_python import I2C
    
#TPS65271 register address
TPS65271_CHIPID     ="0x00"
TPS65271_PPATH      ="0x01"
TPS65271_INT        ="0x02"
TPS65271_CHGCONFIG0 ="0x03"
TPS65271_CHGCONFIG1 ="0x04"
TPS65271_CHGCONFIG2 ="0x05"
TPS65271_CHGCONFIG3 ="0x06"
TPS65271_WLEDCTRL1  ="0x07"
TPS65271_WLEDCTRL2  ="0x08"
TPS65271_MUXCTRL    ="0x09"
TPS65271_STATUS     ="0x0A"
TPS65271_PASSWORD   ="0x0B"
TPS65271_PGOOD      ="0x0C"
TPS65271_DEFPG      ="0x0D"
TPS65271_DEFDCDC1   ="0x0E"
TPS65271_DEFDCDC2   ="0x0F"
TPS65271_DEFDCDC3   ="0x10"
TPS65271_DEFSLEW    ="0x11"
TPS65271_DEFLDO1    ="0x12"
TPS65271_DEFLDO2    ="0x13"
TPS65271_DEFLS1     ="0x14"
TPS65271_DEFLS2     ="0x15"
TPS65271_ENABLE     ="0x16"
TPS65271_DEFUVLO    ="0x17"
TPS65271_SEQ1       ="0x18"
TPS65271_SEQ2       ="0x19"
TPS65271_SEQ3       ="0x1A"
TPS65271_SEQ4       ="0x1B"
TPS65271_SEQ5       ="0x1C"
TPS65271_SEQ6       ="0x1E"

device = I2C()
device.check_i2ctools()

# For some reason writeI2C method doesn't seem to work
#device.writeI2C(TPS65271_CHGCONFIG3, "0xb2")

print "---------------------------"
print "---------REGISTERS---------"
print "---------------------------"
print "TPS65271_CHIPID: "+ bin(int(device.readI2C(TPS65271_CHIPID),16))
print "TPS65271_CHGCONFIG0: "+ bin(int(device.readI2C(TPS65271_CHGCONFIG0),16))
print "TPS65271_CHGCONFIG1: "+ bin(int(device.readI2C(TPS65271_CHGCONFIG1),16))
print "TPS65271_CHGCONFIG2: "+ bin(int(device.readI2C(TPS65271_CHGCONFIG2),16))
print "TPS65271_CHGCONFIG3: "+ bin(int(device.readI2C(TPS65271_CHGCONFIG3),16))
print "TPS65271_DEFUVLO: "+ bin(int(device.readI2C(TPS65271_DEFUVLO),16))
print "---------------------------"

print "checking TERMI:"


"""
    Check TERMI bit (CHCONFIG0[4]) which determines:
"""
def checkTERMI():
    termi0 = "charging, charge termination current threshold has not been crossed"
    termi1 = "charge termination current threshold has been crossed and charging has been stopped. This can be due to a battery reaching full capacity or to a battery removal condition"
    chconfig0 = bin(int(device.readI2C(TPS65271_CHGCONFIG0),16))
    if len(chconfig0) < 5:
        print "TERMI: 0" 
    else:
        TERMI = chconfig0[4]
        print "TERMI: "+ TERMI

checkTERMI()


"""
def node():
    pub = rospy.Publisher('altimeter', String)
    rospy.init_node('mpl2115a2')
    device = I2C()
    device.check_i2ctools()

    # Set to Altimeter with an OSR = 128 
    device.writeI2C(MPL3115_CTRL_REG1, "0xB8")
    # Enable Data Flags in PT_DATA_CFG
    device.writeI2C(MPL3115_PT_DATA_CFG, "0x07")
    # Set Active (polling)
    device.writeI2C(MPL3115_CTRL_REG1, "0xB9")

    while not rospy.is_shutdown():
        # Read STATUS Register
        STA = device.readI2C(MPL3115_STATUS)
        # check if pressure or temperature are ready (both) [STATUS, 0x00 register]
        if STA == "":
            print "error with the sensor"
            break
        if (int(STA,16) & 0x04) == 4:
            # OUT_P
            OUT_P_MSB = device.readI2C("0x01")
            OUT_P_CSB = device.readI2C("0x02")
            OUT_P_LSB = device.readI2C("0x04")
            ## OUT_T
            #OUT_T_MSB = readI2C(0x04)
            #OUT_T_LSB = readI2C(0x05)

            #print OUT_P_MSB
            #print OUT_P_CSB
            #print OUT_P_LSB
    
            #treat the bits to get the altitude
            signedvalue = OUT_P_MSB+OUT_P_CSB[2:]
            fraction = OUT_P_LSB[:3]
    
            #print int(signedvalue,16)
            #print int(fraction,16)

            str = "signedvalue: %s" % signedvalue
            rospy.loginfo(str)
            pub.publish(String(str))

        else:
            #print "data not ready"
            pass
        rospy.sleep(1.0)


if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
"""

