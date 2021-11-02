import sacn


class leds:
    def __init__(self, ip, num_leds):
        self.num_leds = num_leds
        self.data_stream = [0] * (self.num_leds*3)
        # Setup e1.31 sacn sending
        self.sender = sacn.sACNsender()
        self.sender.start()
        self.sender.activate_output(1)
        self.sender[1].destination = ip
        print("E1.31 SACN CONNECTION STARTED")

    def data(self, pixel, rgb):
        self.data_stream[pixel * 3] = rgb[0]
        self.data_stream[(pixel * 3) + 1] = rgb[1]
        self.data_stream[(pixel * 3) + 2] = rgb[2]

    def send_data(self):
        self.sender[1].dmx_data = self.data_stream

    def fill_data(self, rgb):
        for led in range(self.num_leds):
            self.data_stream[led*3] = rgb[0]
            self.data_stream[(led*3) + 1] = rgb[1]
            self.data_stream[(led*3) + 2] = rgb[2]

    def stop_data(self):
        self.sender.stop()
        print("E1.31 SACN CONNECTION STOPPED")
