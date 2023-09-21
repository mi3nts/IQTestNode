
# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
import itertools
import base64
from cgitb import strong
# import imp
# from this import d
import paho.mqtt.client as mqtt
import datetime 
from datetime import timedelta
import yaml
import collections
import json
import time 
import serial.tools.list_ports
from collections import OrderedDict
from glob import glob
from mintsXU4 import mintsDefinitions as mD
# from mintsXU4 import mintsPoLo as mPL
from collections import OrderedDict
import struct
import numpy as np
import pynmea2
import shutil

#import SI1132
from mintsI2c.i2c_bme280   import BME280
from mintsI2c.i2c_scd30    import SCD30
from mintsI2c.i2c_as7265x  import AS7265X
from mintsI2c.i2c_pa101d   import PAI101D_


import math
import sys
import time
import os
import smbus2

debug  = False 

bus     = smbus2.SMBus(0)

scd30   = SCD30(bus,debug)
bme280  = BME280(bus,debug)
as7265x = AS7265X(bus,debug)
pa101d  = PAI101D_(bus,debug)



if __name__ == "__main__":
    
    print()
    print("============ MINTS POLO NODES ============")
    print()
    
    # I2C Devices 
    scd30Online    =  scd30.initiate(30)
    bme280Online   =  bme280.initiate(30)
    as7265xOnline  =  as7265x.initiate()
    pa101dOnline   =  pa101d.initiate()
    # mbls001Onlune  =  mbls001.initiate()
    
    while True:
        try:    
            if as7265xOnline:
                as7265x.readMqtt();
            if bme280Online:
                bme280.readMqtt();
            if pa101dOnline:
                pa101d.readMqtt("GPRMC");                        
            if scd30Online:
                scd30.readMqtt();
            if pa101dOnline:
                pa101d.readMqtt("GPGGA");                        
        

        except Exception as e:
            time.sleep(.5)
            print ("Error and type: %s - %s." % (e,type(e)))
            time.sleep(.5)
        
                  
        
        
        

        
        
        
        
        