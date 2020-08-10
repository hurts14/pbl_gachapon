#!/usr/bin/python
#coding: utf-8
import json
import sys
import RPi.GPIO as GPIO
import signal
import time
import yaml
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

servo = GPIO.PwM(18, 50)

servo.start(0.0)

i = 0

while i < 10:
    servo.ChangeDutyCycle(2.5)
    time.sleep(1)
    servo.ChangeDutyCycle(12)
    time.sleep(1)
    servo.ChangeDutyCycle(2.5)
    time.sleep(3)
    i += 1


