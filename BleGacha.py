# -*- coding: utf-8 -*-
#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import time
import subprocess
import sys
from beacontools import BeaconScanner, BluetoothAddressType, ExposureNotificationFrame

bt_list={}

def callback(bt_addr, rssi, packet, additional_info):
    try:
        print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    
    except:
        print(sys.exc_info())


def moveGacha():
    #path = '//'
    cmd = 'py Servo_20200807.py'
    subprocess.call(cmd, shell = True)


def scan_cocoa():
    
    scanner = BeaconScanner(callback,
                        # remove the following line to see packets from all beacons
                        packet_filter=[ExposureNotificationFrame],
                        scan_parameters={'address_type':BluetoothAddressType.PUBLIC}
                       )
    scanner.start()
    try:
        while True:
            if(0 == len(bt_list)):
                print('<No User Installed Cocoa app>')
            for i in list(bt_list):
                #新しい配列かつ強度が70以上なら
                if(True):
                    print('')
                    moveGacha()
                else:
                    #すでにある
                    print('')
    #time.sleep(10)
    except KeyboardInterrupt:
        scanner.stop()


def main():
    scan_cocoa()
    

if __name__ == "__main__":
    main()
