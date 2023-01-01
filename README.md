# Micropython-Project
Micro-python project on pyboard.


# What does it do?
It starts counting from 0 to 15 (4-bit counter) and then starts over. When the USR button is pushed, *ISR* function will be called.


# *ISR* Function
When switch is pressed, counter is paused and this function: 
1. Counter stops counting
2. Prints the distance of object using **HC-SR04** ultrasonic sensor
3. Specific LED light (R/B/G/Y) starts blinking 3 times based on sensor returned value using handler class
   - RED: 0-49 cm
   - GREEN: 50-99 cm
   - YELLOW: 100-149 cm
   - BLUE: 150<
4. Counter continues counting after LED blinks


# HC-SR04 Sensor
This sensor has 4 pins that we need to worry about:
1. VCC (Power)
2. Trig pulse input
3. Echo pulse output
4. GND (Ground)

We only need to supply a short 10uS pulse to the trigger input to start the ranging, and then the module will send out an 8 cycle burst of ultrasound at 40 kHz and raise its echo. The Echo is a distance object that is pulse width and the range in proportion.
We can calculate the range through the time interval between sending trigger signal and receiving echo signal:
$$Distance = uS / 58 (cm)$$ 

For more information visit: [HC-Sr04 Documentation](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)


