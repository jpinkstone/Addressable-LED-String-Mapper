import board
import neopixel

pixel_pin = board.D18
led_index = 0
num_leds = 50

pixels = neopixel.NeoPixel(pixel_pin, num_leds, brightness=1, auto_write=False)

pixels[led_index] = ((255, 255, 255))
pixels.show()
led_index += 1

while True:
    if input() == 'n' and led_index <= num_leds-1:
        pixels[led_index-1] = (0, 0, 0)
        pixels.show()
        pixels[led_index] = (255, 255, 255)
        pixels.show()
        led_index += 1