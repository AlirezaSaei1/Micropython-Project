# Micropython-Project
---
Micro-python project on pyboard.


# What does it do?
---
It starts counting from 0 to 15 (4-bit counter) and then starts over. When the USR switch is pushed, *calc_distance* function will be called.


# *Calc_distance* Function
---
When switch is pressed, counter is paused and this function:
1. turns on the LED no.4 (BLUE)
2. prints the distance of object using **HC-SR04** ultrasonic sensor
3. Sleeps 1 second
4. turns off the LED
5. counter continues counting


# HC-SR04 Sensor
---
This sensor has 4 pins that we need to worry about:
1. VCC (Power)
2. Trig pulse input
3. Echo pulse output
4. GND (Ground)

We only need to supply a short 10uS pulse to the trigger input to start the ranging, and then the module will send out an 8 cycle burst of ultrasound at 40 kHz and raise its echo. The Echo is a distance object that is pulse width and the range in proportion.
We can calculate the range through the time interval between sending trigger signal and receiving echo signal:
$$Distance = uS / 58 (cm)$$ 

For more information visit: [HC-Sr04 Documentation](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)


