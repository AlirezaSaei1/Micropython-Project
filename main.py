import ultrasonic
import pyb
import time
import micropython

# last exception is tracable by code below (stack trace size == 1)
micropython.alloc_emergency_exception_buf(100)


def calc_distance():
    led.toggle()
    print(f"Distance: {sensor.distance_cm()}")
    time.sleep(1)
    led.toggle()


led = pyb.LED(4)

# run calc_distance function when USR switch is pushed
sw = pyb.Switch()
sw.callback(calc_distance)


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
