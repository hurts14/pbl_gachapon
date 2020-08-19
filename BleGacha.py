# -*- coding: utf-8 -*-
#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import time
import subprocess
import sys
from beacontools import BeaconScanner, BluetoothAddressType, ExposureNotificationFrame

bt_set = set()

def callback(bt_addr, rssi, packet, additional_info):
    global bt_set
    try:
        #強度が70以上ならリストに追加
        print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
        if(70 <= abs(rssi)):
            bt_set.add(bt_addr)
    except:
        print(sys.exc_info())


def moveGacha():
    cmd = 'py moveGacha.py'
    subprocess.call(cmd, shell = True)


def scan_cocoa():
    global bt_set
    gacha_list = set()
    scanner = BeaconScanner(callback,
                        # remove the following line to see packets from all beacons
                        packet_filter=[ExposureNotificationFrame],
                        scan_parameters={'address_type':BluetoothAddressType.PUBLIC}
                       )
    scanner.start()
    try:
        while True:
            if(0 == len(bt_set)):
                print('<No User Installed Cocoa app>')
            for bt in list(bt_set):
                
                if(bt not in gacha_list):
                    print('')
                    moveGacha()
                    gacha_list.add(bt)
                else:
                    #すでにある
                    print('')
            time.sleep(1)
    except KeyboardInterrupt:
        scanner.stop()


def test1():
    global bt_set
    gacha_list = set()
    scanner = BeaconScanner(callback,
                        # remove the following line to see packets from all beacons
                        packet_filter=[ExposureNotificationFrame],
                        scan_parameters={'address_type':BluetoothAddressType.PUBLIC}
                       )
    scanner.start()
    try:
        while True:
            if(0 == len(bt_set)):
                print('<No User Installed Cocoa app>')
            for bt in list(bt_set):
                
                if(bt not in gacha_list):
                    print('now')
                    gacha_list.add(bt)
                else:
                    print('done')
            time.sleep(1)
    except KeyboardInterrupt:
        scanner.stop()  


def main():
    #scan_cocoa()
    test1()
    

if __name__ == "__main__":
    main()
