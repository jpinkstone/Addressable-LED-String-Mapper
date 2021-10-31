import sacn
import time
import random

num_pixels = 50
locations = {}
led_index = 0
data_stream = [0] * 150

def data(pixel, red, green, blue):
    global data_stream
    data_stream[pixel*3] = red
    data_stream[(pixel*3)+1] = green
    data_stream[(pixel*3)+2] = blue

def send_data():
    global data_stream
    sender[1].dmx_data = data_stream

def clear_data():
    global data_stream
    data_stream = [0] * 150

sender = sacn.sACNsender()
sender.start()
sender.activate_output(1)
sender[1].destination = "192.168.1.2"

with open('led_locs.txt') as file:
    content = file.readlines()
content = [x.strip() for x in content]

for led in content:
    locations[led_index] = eval(led)
    led_index += 1

order_x = dict(sorted(locations.items(), key=lambda x: x[1][0], reverse=True))
order_y = dict(sorted(locations.items(), key=lambda x: x[1][1], reverse=True))

clear_data()
send_data()

def wipe_x(color):
    for value in order_x:
        if value <= num_pixels-3:
            data(value, color[0], color[1], color[2])
            data(value+1, color[0], color[1], color[2])
            data(value+2, color[0], color[1], color[2])
            send_data()
            time.sleep(0.1)
            clear_data()
            send_data()

def wipe_y(color):
    for value in order_y:
        if value <= num_pixels-3:
            data(value, color[0], color[1], color[2])
            data(value + 1, color[0], color[1], color[2])
            data(value + 2, color[0], color[1], color[2])
            send_data()
            time.sleep(0.1)
            clear_data()
            send_data()

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

sender.stop()