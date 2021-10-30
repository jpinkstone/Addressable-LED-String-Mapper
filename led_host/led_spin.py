import board
import neopixel
import time
import math

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

heights = []
for i in locations:
    heights.append(locations[i][1])

min_alt = min(heights)
max_alt = max(heights)

dinc = 1
buffer = 100
slow = 0.05
angle = 0
inc = 0.1
colourA = [0,255,255]
colourB = [255,255,0]

swap01 = 0
swap02 = 0
direction = -1
c = 200

while True:
    
    time.sleep(slow)
    
    LED = 0
    while LED < num_pixels:
        if math.tan(angle)*locations[LED][0] <= locations[LED][1]+c:
            pixels[LED] = colourA
        else:
            pixels[LED] = colourB
        LED += 1
    
    pixels.show()

    angle += inc
    if angle > 2*math.pi:
        angle -= 2*math.pi
        swap01 = 0
        swap02 = 0
    
    if angle >= 0.5*math.pi:
        if swap01 == 0:
            colour_hold = [i for i in colourA]
            colourA =[i for i in colourB]
            colourB = [i for i in colour_hold]
            swap01 = 1
            
    if angle >= 1.5*math.pi:
        if swap02 == 0:
            colour_hold = [i for i in colourA]
            colourA =[i for i in colourB]
            colourB = [i for i in colour_hold]
            swap02 = 1

    c += direction*dinc
    
    if c <= min_alt+buffer:
        direction = 1
    if c >= max_alt-buffer:
        direction = -1