# -*- coding: utf-8 -*-
#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import time
import subprocess
#from beacontools import BeaconScanner, EddystoneTLMFrame, EddystoneFilter
from beacontools import BeaconScanner, IBeaconFilter

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))


def moveGacha():
    #path = '//'
    cmd = 'py Servo_20200807.py'
    subprocess.call(cmd, shell = True)


def main():
    scanner = BeaconScanner(callback,
                        # remove the following line to see packets from all beacons
                        device_filter=IBeaconFilter(uuid="0000fd6f-0000-1000-8000-00805f9b34fb")#[0xFD6F]
                       )
    scanner.start()
    time.sleep(10)
    scanner.stop()
    

if __name__ == "__main__":
    main()
