from leds_class import leds
import time

pixels = leds("192.168.1.2", 50)

while True:
    #Simple test lighting up every pixel individually
    for led in range(50):
        pixels.data(led, [255, 255, 0])
        pixels.send_data()
        time.sleep(1)
    pixels.fill_data([0, 0, 0])

pixels.stop_data()
