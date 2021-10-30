import board
import neopixel
import time
import random

pixel_pin = board.D18
num_pixels = 50
locations = {}
led_index = 0

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)

with open('led_locs.txt') as file:
    content = file.readlines()
content = [x.strip() for x in content]

for led in content:
    locations[led_index] = eval(led)
    led_index += 1

order_x = dict(sorted(locations.items(), key=lambda x: x[1][0], reverse=True))
order_y = dict(sorted(locations.items(), key=lambda x: x[1][1], reverse=True))

pixels.fill((0, 0, 0))
pixels.show()

def wipe_x(color):
    for value in order_x:
        if value <= num_pixels-3:
            pixels[value] = color
            pixels[value+1] = color
            pixels[value+2] = color
            pixels.show()
            time.sleep(0.1)
            pixels.fill((0, 0, 0))
            pixels.show()

def wipe_y(color):
    for value in order_y:
        if value <= num_pixels-3:
            pixels[value] = color
            pixels[value+1] = color
            pixels[value+2] = color
            pixels.show()
            time.sleep(0.1)
            pixels.fill((0, 0, 0))
            pixels.show()

def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

while True:
    wipe_x(wheel(random.randint(0, 255)))
    time.sleep(0.5)
    wipe_y(wheel(random.randint(0, 255)))
    time.sleep(0.5)