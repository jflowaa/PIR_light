#!/usr/bin/env python
from light import LightControl
from Adafruit_BBIO import GPIO
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

turn_off_time = current_time  = datetime.now()
print("Starting System")
print("Offset is set at {} minutes.".format(args.offset))
while True:
    try:
        if current_time >= turn_off_time:
            lightcontrol.turn_off()
        if GPIO.event_detected(args.PIR):
            lightcontrol.turn_on()
            turn_off_time = datetime.now() + timedelta(minutes=args.offset)
        current_time = datetime.now()
        time.sleep(1)
    except:
        try:
            lightcontrol = LightControl(args.IP, 5577)
        except:
            time.sleep(15)
