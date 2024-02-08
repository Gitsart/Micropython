import machine
import time

# Define the pin number of the built-in LED
led_pin = 2  # On ESP32, the built-in LED is usually connected to pin 2

# Set the pin as an output
led = machine.Pin(led_pin, machine.Pin.OUT)

# Blink the LED
while True:
    led.value(1)  # Turn on the LED (1 means high, 0 means low)
    time.sleep(0.5)  # Wait for 0.5 seconds
    led.value(0)  # Turn off the LED
    time.sleep(0.5)  # Wait for 0.5 seconds
