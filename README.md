# Addressable LED String Mapper

This project maps RGB LED string pixels to a 2D plane for easier animation creation.

## Components
 - Host ESP8266 NodeMCU running WLED controlling the LED pixel string
 - Laptop with webcam to record pixel locations and send data

## Setup
 - Install WLED on the ESP8266 NodeMCU and connect to LED string. Make sure e1.31 protocol is enabled and record ip address
 - Place the led_mapper.py on the laptop, change the num_leds to be correct, change the cv2.VideoCapture() first argument to 0 for the internal webcam or 1 for an external webcam, and change the ip address to that of the ESP8266 NodeMCU controller.

## Instructions

- Point webcam at the full array of LED pixels
- Start the mapper script on the laptop, click the Space Bar to start
- Wait until each pixel is lit up and location recorded
- When the scripts are finished, there will be a txt file on the laptop with LED pixel locations
