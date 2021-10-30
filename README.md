# Addressable LED String Mapper

This project maps RGB LED string pixels to a 2D plane for easier animation creation.

## Components
 - Host Raspberry Pi controlling the LED pixel string
 - Laptop with webcam to record pixel locations

## Setup
 - Place led_mapper_host.py on the Raspberry Pi and change the num_leds to be correct
 - Place the led_mapper.py on the laptop, change the num_leds to be correct, and change the cv2.VideoCapture() first argument to 0 for the internal webcam or 1 for an external webcam

## Instructions

- Point webcam at the full array of LED pixels
- SSH into the host Raspberry Pi controlling the LED pixels and start the mapper script
- Start the mapper script on the laptop, click the Space Bar to start, and click into the SSH terminal
- Wait until each pixel is lit up and location recorded
- When the scripts are finished, there will be a txt file on the laptop with LED pixel locations
