import sacn
import time

num_leds = 50
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

while True:
    #Simple test lighting up every pixel individually
    for led in range(50):
        data(led, 255, 0, 0)
        send_data()
        time.sleep(1)
    clear_data()

sender.stop()