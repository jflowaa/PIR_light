# PIR Sensor With WiFi Light Bulb
A simple project to create your own motion light

When motion is detected the light bulb will turn on. After a set amount of time of no motion the light bulb will turn off.
#### Getting Started
This program relys on a [PIR sensor](http://www.amazon.com/Leegoal-Pyroelectric-Infrared-Motion-Detector/dp/B008AESDSY), [Flux WiFi light bulb](http://www.amazon.com/Flux-WiFi-Smart-Light-Bulb/dp/B00SGLKWQW), and a beaglebone black. Any PIR sensor could be used and a raspberry pi could also be used instead. Just have to switch the adafruit's BB library to rPI library. Other wifi light bulbs won't work without a large amount of tuning. 
### How To Run:
> ./run.py -h
 
 Will give argument listings.
  
  > ./run.py "192.168.1.20" 30
   
   Will set the IP and the offset of the shutoff time.
    
    > ./run.py "192.168.1.20" 30 -pin "P9_23"
     
     This sets the pinout from the default of "P9_12" to "P9_23"

     #### TO DO
     * Schedule a time range when system is active
