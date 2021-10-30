import board
import neopixel
import time
import random
import math

pixel_pin = board.D18
num_pixels = 50

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)

def clearAll():
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
 
 
def color_chase(color):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(0.05)
        pixels.show()
    time.sleep(0.5)
 
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def cylon_bounce(color, size):
    for i in range(num_pixels - size - 2):
        clearAll()
        pixels[i] = (color[0]/10, color[1]/10, color[2]/10)
        for j in range(1, size):
            pixels[i+j] = color
        pixels[i+size+1] = (color[0]/10, color[1]/10, color[2]/10)
        pixels.show()
        time.sleep(0.05)

    time.sleep(1)

    for i in range(num_pixels - size - 2, 0, -1):
        clearAll()
        pixels[i] = (color[0]/10, color[1]/10, color[2]/10)
        for j in range(1, size):
            pixels[i+j] = color
        pixels[i+size+1] = (color[0]/10, color[1]/10, color[2]/10)
        pixels.show()
        time.sleep(0.05)

    time.sleep(1)

def twinkle(color):
    clearAll()
    for i in range(num_pixels):
        pixels[random.randint(0, num_pixels-1)] = color
        pixels.show()
        time.sleep(0.05)

def sparkle():
    for x in range(num_pixels*10):
        pixel = random.randint(0, num_pixels-1)
        pixels[pixel] = (255, 255, 255)
        pixels.show()
        time.sleep(0.01)
        pixels[pixel] = (0, 0, 0)

def running_lights(color):
    position = 0
    for i in range(0, num_pixels*2):
        position += 1
        for j in range(0, num_pixels):
            pixels[j] = (((math.sin(j+position)*127+128)/255)*color[1], ((math.sin(j+position)*127+128)/255)*color[0], ((math.sin(j+position)*127+128)/255)*color[2])
        pixels.show()
        time.sleep(0.05)

while True:
    clearAll()
    color_chase((0, 255, 0))
    color_chase((170, 245, 65))
    color_chase((245, 245, 65))
    color_chase((255, 0, 0))
    color_chase((0, 0, 255))
    color_chase((65, 175, 245))
    clearAll()
    rainbow_cycle(0.01)
    clearAll()
    for x in range(0, 250, 50):
        cylon_bounce(wheel(x), 5)
    clearAll()
    for x in range(0, 250, 50):
        twinkle(wheel(x))
    clearAll()
    sparkle()
    clearAll()
    for x in range(0, 250, 50):
        running_lights(wheel(x))
    clearAll()