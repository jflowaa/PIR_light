#!/usr/bin/env python
from light import LightControl
import Adafruit_BBIO.GPIO as GPIO
from datetime import datetime, timedelta
import time
import argparse

parser = argparse.ArgumentParser(description="Light Motion Detector", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-pin", type=str, help="GPIO pin of sensor", default="P9_12", dest="PIR")
parser.add_argument("IP", type=str, help="IP of WiFi lightbulb")
parser.add_argument("offset", type=int, help="How long the light stays on")
parser.add_argument("-schedule", type=bool, help="Run system on schedule?", default=False)
args = parser.parse_args()

if args.schedule:
    print("TODO: Schedule feature")

GPIO.setup(args.PIR, GPIO.IN)
GPIO.add_event_detect(args.PIR, GPIO.RISING)
lightcontrol = LightControl(args.IP, 5577)

time_to_turn_off = time  = datetime.now()
print("Starting System")
print("Offset is set at {} minutes.".format(args.offset))
while True:
    if time >= time_to_turn_off:
        lightcontrol.turn_off()
    if GPIO.event_detected(args.PIR):
        time_to_turn_off = datetime.now() + timedelta(minutes=args.offset) 
        lightcontrol.turn_on()
    time = datetime.now()
