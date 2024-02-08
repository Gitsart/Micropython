import machine
import time

# Set up UART and button GPIO
uart = machine.UART(2, baudrate=9600, tx=17, rx=16)  # Specify UART2, TX on GPIO 17, RX on GPIO 16
button1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)  # GPIO 5 as input with pull-up resistor

def send_data(data):
    uart.write(data)

while True:
    if button1.value() == 0:  # Button is pressed (GND)
        send_data("Forward...\n")
        time.sleep(2)
