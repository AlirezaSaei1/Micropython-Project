import time


class Handler(object):
    def __init__(self, led):
        self.led = led
        self.cb()

    def cb(self):
        self.led.off()
        for _ in range(6):
            self.led.toggle()
            time.sleep(0.3)
