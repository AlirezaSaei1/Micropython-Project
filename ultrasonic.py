from time import sleep_us
from machine import Pin, time_pulse_us


class Ultrasonic(object):
    def __init__(self, trigger_pin, echo_pin, timeout_us=30000):
        self.timeout = timeout_us

        # Initialize trig pins
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.off()

        # Initialize echo pins
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

    def distance_cm(self):
        # Send a 10us pulse
        self.trigger.on()
        sleep_us(10)
        self.trigger.off()

        time_pulse = time_pulse_us(self.echo, 1, self.timeout)

        if time_pulse < 0:
            raise Exception(f"Timeout: {self.timeout} us")

        # time pulse is RTT must be divided by 2 then divide it
        # by 29 us/cm ~ 340 m/s
        return (time_pulse / 2) / 29
