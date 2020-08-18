# -*- coding: utf-8 -*-
#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import time
import subprocess
#from beacontools import BeaconScanner, EddystoneTLMFrame, EddystoneFilter
from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement, BluetoothAddressType, ExposureNotificationFrame

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))


def moveGacha():
    #path = '//'
    cmd = 'py Servo_20200807.py'
    subprocess.call(cmd, shell = True)
    #cc:2d:b7:94:6b:81


def scan_cocoa():
    
    scanner = BeaconScanner(callback,
                        # remove the following line to see packets from all beacons
                        #device_filter=IBeaconFilter(uuid="0000fd6f-0000-1000-8000-00805f9b34fb"),#[0xFD6F]
                        #packet_filter=IBeaconAdvertiesment,
                        packet_filter=[ExposureNotificationFrame],
                        scan_parameters={'address_type':BluetoothAddressType.PUBLIC}
                       )

    scanner.start()
    time.sleep(10)
    scanner.stop()


def scan_ble():
    print('yes')

def main():
    scan_cocoa()
    

if __name__ == "__main__":
    main()
