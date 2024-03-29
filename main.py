import ultrasonic
import pyb
import time
import micropython
from handler import Handler

# last exception is tracable by code below (stack trace size == 1)
micropython.alloc_emergency_exception_buf(100)


def ISR():
    dist = calc_distance()

    if 0 <= dist < 50:
        red = Handler(pyb.LED(1))
    elif 50 <= dist < 100:
        grn = Handler(pyb.LED(2))
    elif 100 <= dist < 150:
        ylw = Handler(pyb.LED(3))
    else:
        blue = Handler(pyb.LED(4))


def calc_distance():
    x = sensor.distance_cm()
    print(f"Distance: {x}")
    return x


# run calc_distance function when USR switch is pushed
sw = pyb.Switch()
sw.callback(ISR)


sensor_trig_pin = pyb.Pin.board.X3
sensor_echo_pin = pyb.Pin.board.X4
sensor = ultrasonic.Ultrasonic(sensor_trig_pin, sensor_echo_pin)

# counter increases from 0 to 15 (1 every second) and then resets (4-bit counter)
counter = 0
while True:
    if (counter == 16):
        counter = 0

    print(f"Counter: {counter}")
    counter = counter + 1
    time.sleep(1)
